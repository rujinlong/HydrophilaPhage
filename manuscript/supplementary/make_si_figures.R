#!/usr/bin/env Rscript
# Generate supplementary figures for the Hp3 manuscript from analysis outputs.
# Outputs (in this dir, included by supplementary.tex):
#   si_fig_phrog.png       -- Figure S2: PHROG functional-category distribution (105 ORFs)
#   si_fig_viptree_sg.png  -- Figure S3: ViPTree whole-proteome similarity (S_G) to Hp3
# Inputs live in the gitignored Dropbox data tree (analyses/data is a symlink).
# Re-run:  Rscript make_si_figures.R
suppressPackageStartupMessages(library(ggplot2))

DATA <- path.expand("~/Dropbox/project/pc031-aquaPhage/data")
HERE <- tryCatch(dirname(sub("^--file=", "",
          grep("^--file=", commandArgs(FALSE), value = TRUE)[1])),
        error = function(e) ".")
if (is.na(HERE) || HERE == "") HERE <- "."

## ---- Figure S2: PHROG functional-category distribution -------------------
orf <- read.delim(file.path(DATA, "submit/submit-fsi/Hp3_ORF_annotation.tsv"),
                  check.names = FALSE)
cats <- table(orf[["function"]])
pretty <- function(x) {
  x <- gsub("DNA, RNA and nucleotide metabolism", "DNA/RNA & nucleotide metabolism", x, fixed = TRUE)
  x <- gsub("moron, auxiliary metabolic gene and host takeover", "moron/AMG & host takeover", x, fixed = TRUE)
  x <- gsub("integration and excision", "integration & excision", x, fixed = TRUE)
  x <- gsub("head and packaging", "head & packaging", x, fixed = TRUE)
  x <- gsub("transcription regulation", "transcription regulation", x, fixed = TRUE)
  x
}
df <- data.frame(category = pretty(names(cats)), n = as.integer(cats))
df <- df[order(df$n), ]
df$category <- factor(df$category, levels = df$category)

p1 <- ggplot(df, aes(n, category)) +
  geom_col(fill = "#2C7FB8", width = 0.7) +
  geom_text(aes(label = n), hjust = -0.35, size = 3) +
  scale_x_continuous(expand = expansion(mult = c(0, 0.12))) +
  labs(x = "Number of ORFs", y = NULL) +
  theme_bw(base_size = 11) +
  theme(panel.grid.major.y = element_blank(),
        panel.grid.minor = element_blank())
ggsave(file.path(HERE, "si_fig_phrog.png"), p1, width = 7, height = 3.6, dpi = 300)
cat(sprintf("[ok] si_fig_phrog.png  (%d ORFs, %d categories)\n", sum(df$n), nrow(df)))

## ---- Figure S3: ViPTree whole-proteome similarity (S_G) to Hp3 -----------
sg <- read.delim(file.path(DATA, "ICTV_proposal/03_similarity_matrices/viptree_SG_to_hp3.tsv"),
                 check.names = FALSE)
col <- grep("to hp3", names(sg), value = TRUE)[1]
v <- suppressWarnings(as.numeric(sg[[col]]))
v <- v[!is.na(v) & v < 0.99]                 # drop the S_G = 1.0 self-hit (Hp3 query)
v <- sort(v, decreasing = TRUE)
d <- data.frame(rank = seq_along(v), sg = v)
n_above <- sum(v > 0.02)

p2 <- ggplot(d, aes(rank, sg)) +
  geom_line(colour = "#2C7FB8", linewidth = 0.5) +
  geom_point(data = d[1, ], aes(rank, sg), colour = "#D7301F", size = 2) +
  annotate("text", x = nrow(d) * 0.20, y = v[1],
           label = sprintf("italic(S)[G]^max == %.3f", v[1]), parse = TRUE,
           hjust = 0, vjust = 0.4, size = 3.3, colour = "#D7301F") +
  annotate("text", x = nrow(d) * 0.5, y = 0.045,
           label = sprintf("Only %d of %s references exceed 0.02",
                           n_above, format(length(v), big.mark = ",")),
           hjust = 0.5, size = 3.1, colour = "grey25") +
  labs(x = sprintf("Reference prokaryotic dsDNA virus (ranked by similarity, n = %s)",
                   format(length(v), big.mark = ",")),
       y = expression("Whole-proteome similarity " * S[G] * " to Hp3")) +
  theme_bw(base_size = 11) +
  theme(panel.grid.minor = element_blank())
ggsave(file.path(HERE, "si_fig_viptree_sg.png"), p2, width = 7, height = 3.6, dpi = 300)
cat(sprintf("[ok] si_fig_viptree_sg.png  (n=%d refs, max S_G=%.3f, %d > 0.02)\n",
            length(v), v[1], n_above))
