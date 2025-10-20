parse_vcontact3 <- function(fin_vcontact3) {
  # fin_vcontact3: final_assignments.csv
  df <- fread(fin_vcontact3) %>%
    data.table::setnames(c("Genome"), c("repid")) %>%
    dplyr::mutate(
      vcontact3_genus = ifelse(genus_prediction == "", repid, genus_prediction)
    ) %>%
    # dplyr::select(c("index", "repid", "vcontact3_genus", "Reference")) %>%
    dplyr::mutate(
      vcontact3_classified = ifelse(
        vcontact3_genus == repid,
        "unclassified",
        "classified"
      )
    )

  vc_ids <- df %>%
    dplyr::select("vcontact3_genus") %>%
    dplyr::distinct() %>%
    # add new column "VC" to the data frame, and fill it with the value "VC" and the number of rows
    dplyr::mutate(VC_id = paste0("VC", 1:nrow(.)))

  df_vc <- df %>%
    dplyr::left_join(vc_ids, by = "vcontact3_genus")

  df_vc_with_ref <- df_vc %>%
    dplyr::filter(Reference == "TRUE") %>%
    dplyr::select("VC_id") %>%
    dplyr::distinct()

  df_vcontact3 <- df_vc %>%
    dplyr::mutate(
      VC_with_ref = ifelse(VC_id %in% df_vc_with_ref$VC_id, "TRUE", "FALSE")
    ) %>%
    dplyr::mutate(
      qry_novel_genus = ifelse(
        str_detect(vcontact3_genus, "^novel_") & VC_with_ref == "FALSE",
        "TRUE",
        "FALSE"
      )
    ) %>%
    # convert column names to valid variable names
    data.table::setnames(colnames(.), make.names(colnames(.)))

  return(df_vcontact3)
}
