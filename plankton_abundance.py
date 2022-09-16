
# GEOMAR Helmholtz Centre for Ocean Research, Kiel, Germany
# Proejct: SFB 754, February 2019
# Sahed Ahmed Palash, Research Assistant

# plankton biomass and abundance analytics using large and medium plankton data
import pandas as pd

# loading the initial files and explore
df_large = pd.read_csv("/home/sahed/Desktop/office/2.m138t_mn_midi_dataframe_large.txt", "\t")
print(df_large.head())
print(df_large.shape)
print(df_large.info)
print(df_large.describe())

df_medium = pd.read_csv("/home/sahed/Desktop/office/3. m138t_mn_midi_dataframe_medium.txt", "\t")
print(df_large.head())
print(df_large.shape)
print(df_large.info)
print(df_large.describe())

# merging initial dataframe which contains plankton variables
df_merged = pd.merge(df_large, df_medium, how="left", on=["haul", "net", "category", "D_N"])
df_merged = df_merged.fillna(0)
df_final = df_merged.reset_index()

# create a new df from a dict and merge it with previous df
data = {

    "haul": ["mn01", "mn02", "mn03", "mn04",
             "mn05", "mn06", "mn07", "mn08",
             "mn09", "mn10", "mn11", "mn12",
             "mn13", "mn14", "mn15", "mn16"],

    "on_off": ["offshore", "offshore", "onshore", "onshore",
               "offshore", "offshore", "onshore", "onshore",
               "onshore", "onshore", "offshore", "offshore",
               "onshore", "onshore", "offshore", "offshore"]
}
on_off_df = pd.DataFrame.from_dict(data)
df_final = pd.merge(df_final, on_off_df, on="haul", how="left")

# add abundance and biomass variables
df_final["abundance"] = df_final['abundance_x'] + df_final['abundance_y']
df_final["biomass"] = df_final['biomass_x'] + df_final['biomass_y']
df_final = df_final.drop(df_final.columns[
                             [0, 1, 2, 6, 7, 8, 11, 15, 16, 19, 20,
                              21, 22, 23, 24, 25, 26, 27, 28, 29,
                              30, 31, 32, 33, 34, 35, 36, 37]], axis=1)

# rename a couple of variables
df_final.rename(columns=
                {'o2_x': 'o2',
                 'temp_x': 'temp',
                 "salinity_x": "salinity",
                 "volume_x": "volume",
                 'depth_x': 'depth',
                 "delta_values_x": "depth_layer"}, 
                inplace=True)

# create a dictionary to have longitude and latitude data
lat_long_df = {"haul":
                   ["mn01", "mn02", "mn03", "mn04",
                    "mn05", "mn06", "mn07", "mn08",
                    "mn09", "mn10", "mn11", "mn12",
                    "mn13", "mn14", "mn15", "mn16"],

               "latitude": [-10.888, -10.951, -10.761, -10.778,
                            -12.412, -12.414, -12.212, -12.212333,
                            -14.001, -14.0015, -14.297, -14.277,
                            -15.424, -15.430, -15.861, -15.860],

               "longitude": [-78.5685, -78.564, -78.271, -78.270,
                             -77.813, -77.812, -77.439, -77.439,
                             -76.660, -76.660, -77.169, -77.177,
                             -75.444, -75.44, -76.105, -76.106]
              }

lats_logs_df2 = pd.DataFrame.from_dict(lat_long_df)
df_final=pd.merge(df_final, lats_logs_df2, on="haul", how="outer")
df_final= df_final.reset_index()

# calculate integrated abundances
df_final["integrated_abundance"] = df_final.abundance*df_final.depth_layer

# calculate integrated biomass
df_final["integrated_biomass"] = df_final.biomass*df_final.depth_layer

# saving the dataframe as a text file
df_final.to_csv("plankton_biomass_final_df.txt", sep="\t", encoding="utf-8")
