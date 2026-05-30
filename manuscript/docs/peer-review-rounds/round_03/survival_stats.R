suppressPackageStartupMessages({library(survival); library(dplyr); library(reshape2)})
fp <- "analyses/data/submit/SupplementalData.xlsx"
raw <- openxlsx::read.xlsx(fp, sheet="survival_curve")
cat("== raw sheet head ==\n"); print(head(raw)); cat("cols:", paste(colnames(raw),collapse=", "), "\n\n")
df <- melt(raw, id.vars="time", variable.name="Group", value.name="Count")

reconstruct <- function(dfc, total_n=20, end_day=7){
  out <- data.frame()
  for(grp in unique(dfc$Group)){
    g <- dfc %>% filter(Group==grp) %>% arrange(time)
    cur <- total_n; deaths <- c()
    for(i in 1:nrow(g)){ d<-g$time[i]; s<-g$Count[i]; nd<-cur-s; if(nd>0) deaths<-c(deaths,rep(d,nd)); cur<-s }
    cens <- rep(end_day, cur)
    out <- rbind(out, data.frame(time=c(deaths,cens), status=c(rep(1,length(deaths)),rep(0,length(cens))), group=grp))
  }
  out
}
sd4 <- reconstruct(df)
ord <- c("PBS_group","phage_group","bacterial_group","treatment_group")
sd4$group <- factor(sd4$group, levels=ord[ord %in% unique(sd4$group)])

cat("== final survivors / deaths per group (of 20) ==\n")
print(sd4 %>% group_by(group) %>% summarise(n=n(), deaths=sum(status), survivors=sum(status==0), surv_pct=round(100*mean(status==0),1)))

cat("\n== OVERALL k-sample log-rank (all groups) ==\n")
ov <- survdiff(Surv(time,status)~group, data=sd4)
print(ov)
cat(sprintf("Overall: Chi-sq=%.3f, df=%d, p=%.3g\n", ov$chisq, length(ov$n)-1, 1-pchisq(ov$chisq,length(ov$n)-1)))

cat("\n== PAIRWISE log-rank (BH-adjusted) ==\n")
prs <- combn(levels(sd4$group),2,simplify=FALSE)
res <- lapply(prs, function(pr){ sub<-sd4%>%filter(group%in%pr); sub$group<-droplevels(sub$group)
  s<-survdiff(Surv(time,status)~group,data=sub); data.frame(pair=paste(pr,collapse=" vs "), chisq=round(s$chisq,3), p_raw=1-pchisq(s$chisq,1)) })
res <- do.call(rbind,res); res$p_BH <- p.adjust(res$p_raw, method="BH")
res$p_raw <- signif(res$p_raw,3); res$p_BH <- signif(res$p_BH,3); print(res, row.names=FALSE)

cat("\n== Cox PH: Hazard Ratio treatment vs bacterial (ref=bacterial) ==\n")
sub <- sd4 %>% filter(group %in% c("bacterial_group","treatment_group")); sub$group<-relevel(droplevels(sub$group),ref="bacterial_group")
cx <- coxph(Surv(time,status)~group, data=sub); s<-summary(cx)
cat(sprintf("HR(treatment vs bacterial)=%.3f, 95%% CI %.3f-%.3f, p=%.3g\n",
  s$conf.int[1,"exp(coef)"], s$conf.int[1,"lower .95"], s$conf.int[1,"upper .95"], s$coefficients[1,"Pr(>|z|)"]))
cat("(HR<1 => treatment reduces hazard of death)\n")
