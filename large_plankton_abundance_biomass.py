
# GEOMAR Helmholtz Centre for Ocean Research Kiel, Germany
# Project: SFB 754, January 2019
# Sahed Ahmed Palash, Research Assistant

# merging cruise_metadata with plankton data
import pandas as pd

# load plankton file
plankton_count_df = pd.read_csv("/home/sahed/Desktop/office/2.ecotaxa_export_large.csv", "\t")
plankton_count_df = pd.DataFrame(
    {
    "category": plankton_count_df["object_annotation_category"],
    "haul_net_id": plankton_count_df["process_id"],
    "area": plankton_count_df["object_area"]
}
)

# extract haul and net naming variables
plankton_count_df["count"] = 1
net_d = plankton_count_df["haul_net_id"].str.split("_", expand=True)[3]
plankton_count_df["net"] = net_d
haul_d = plankton_count_df["haul_net_id"].str.split("_", expand=True)[2]
plankton_count_df["haul"] = haul_d

# group and sort df
plankton_grouped_df = plankton_count_df.groupby(["haul", "net", "category", "area"]).count()
plankton_sorted_df = plankton_count_df.loc[plankton_count_df['category'].isin([
    "Calanoida", "Eucalanidae",
    "Oithona", "Euphausiacea",
    "Pleuroncodes"]).reset_index(drop=True)]
plankton_sorted_df = plankton_sorted_df.reset_index()
plankton_sorted_grouped_df = plankton_sorted_df.groupby(["haul", "net", "category"]).sum()
plankton_sorted_grouped_df = plankton_sorted_grouped_df.reset_index()

# create a dict of image slope and intercept
biomass_dict = {
    "Calanoida": [43.38, 1.54],
    "Oithona": [43.38, 1.54],
    "Pleuroncodes": [43.97, 1.52],
    "Eucalanidae": [43.38, 1.54],
    "Euphausiacea": [49.58, 1.48]
}

# convert area (pixel) into mm⁻², area is in pixel which is the magical number 0.00011236 µm
fn = lambda row: biomass_dict[row["category"]][0]*row["area"]*0.00011236**biomass_dict[row["category"]][1]
col1 = plankton_sorted_grouped_df.apply(fn, axis=1)
plankton_sorted_grouped_df = plankton_sorted_grouped_df.assign(biomass_cal=col1.values)

# load metadata file and get rid of unnecessary naming stuffs
metadata_df = pd.read_csv("/home/sahed/Desktop/office/1.meanData_mn_towed.txt", "\t")
haul_id = metadata_df["haul"].str.split("_", expand=True)[1]
metadata_df["haul"] = haul_id
haul_id_1 = metadata_df["haul"].str.split(".", expand=True)[0]
metadata_df["haul"] = haul_id_1
metadata_df['net'] = 'n' + metadata_df['net'].astype(str)

# merge plankton and metadata df
plankton_metadata_merged = pd.merge(plankton_sorted_grouped_df, metadata_df,  how='left', on=['haul', 'net'])
plankton_metadata_merged = plankton_metadata_merged.reset_index()
plankton_metadata_merged = plankton_metadata_merged.drop('index', 1)

# create a dict for day and night hauls and merge with previous df
data = {
    "haul":
        ["mn01", "mn02", "mn03", "mn04",
         "mn05", "mn06", "mn07", "mn08",
         "mn09", "mn10", "mn11", "mn12",
         "mn13", "mn14", "mn15", "mn16"],

    "D_N":
        ["D", "N", "D", "N",
         "N", "D", "N", "D",
         "N", "D", "D", "N",
         "D", "N", "D", "N"]
}

DN_df = pd.DataFrame.from_dict(data)
plankton_final_df = pd.merge(plankton_metadata_merged, DN_df, how="left", on="haul")

# calculate plankton abundance (formula: abundance=total count/volume of water [L⁻¹])
fn = lambda row: row["count"]/row["volume"]
col2 = plankton_final_df.apply(fn, axis=1)
plankton_final_df = plankton_final_df.assign(abundance=col2.values)

# function to calculate biomass (formula: biomass/volume [µg/m⁻³])
fn = lambda row: row["biomass_cal"]/row["volume"]
col3 = plankton_final_df.apply(fn, axis=1)
df_final = plankton_final_df.assign(biomass=col3.values)

# saving the dataframe in a plain text format file
df_final.to_csv("large_plankton_final_df.txt", sep="\t", encoding="utf-8")
