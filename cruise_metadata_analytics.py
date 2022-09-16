
# GEOMAR Helmholtz Centre for Ocean Research, Kiel, Germany
# Project: SFB 754, January 2019
# Sahed Ahmed Palash, Research Assistant

# extract environmental variables from cruise metadata
import pandas as pd

# loading cruise metadata file and explore
metadata_df = pd.read_csv("/home/sahed/Desktop/office/1.meanData_mn_towed.txt", "\t")
print(metadata_df.head())
print(metadata_df.shape)
print(metadata_df.info)
print(metadata_df.describe())

# split the haul variables to delete "-" and ".text"
haul_id = metadata_df["haul"].str.split("_", expand=True)[1]
metadata_df["haul"] = haul_id
haul_id_1 = metadata_df["haul"].str.split(".", expand=True)[0]
metadata_df["haul"] = haul_id_1

# create a dict for day and night hauls and merge with previous df
D_N_dict = {
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

D_N_df = pd.DataFrame.from_dict(D_N_dict)
metadata_df = pd.merge(metadata_df, D_N_df, how="left", on="haul")

# create another dict for latitudinal and longitudinal data and merge with previous df
lat_long_dict = {
    "haul":
        ["mn01", "mn02", "mn03", "mn04",
         "mn05", "mn06", "mn07", "mn08",
         "mn09", "mn10", "mn11", "mn12",
         "mn13", "mn14", "mn15", "mn16"],

    "latitude":
        [-10.888, -10.951, -10.761, -10.778,
         -12.412, -12.414, -12.212, -12.212333,
         -14.001, -14.0015, -14.297, -14.277,
         -15.424, -15.430, -15.861, -15.860],

    "longitude":
        [-78.5685, -78.564, -78.271, -78.270,
         -77.813, -77.812, -77.439, -77.439,
         -76.660, -76.660, -77.169, -77.177,
         -75.444, -75.44, -76.105, -76.106]
}

lats_logs_df = pd.DataFrame.from_dict(lat_long_dict)
metadata_df = pd.merge(metadata_df, lats_logs_df, on="haul", how="left")

# create another dict for station data and merge with previous df
station_dict = {
    "haul":
        ["mn01", "mn02", "mn03", "mn04",
         "mn05", "mn06", "mn07", "mn08",
         "mn09", "mn10", "mn11", "mn12",
         "mn13", "mn14", "mn15", "mn16"],

    "station":
        ["station 1", "station 1", "station 2", "station 2",
         "station 3", "station 3", "station 4", "station 4",
         "station 6", "station 6", "station 5", "station 5",
         "station 8", "station 8", "station 7", "station 7"]
}
station_df = pd.DataFrame.from_dict(station_dict)
metadata_df = pd.merge(metadata_df, station_df, on="haul", how="left")

# creating a final dataframe and save it
metadata_df.to_csv("metadata_final.txt", sep="\t", encoding="utf-8")
