# Sahed Ahmed Palash, Biological Oceanography, GEOMAR
# Master Thesis, Data Analysis
# mutinet meandata processing vertical huals

# impoting necessary packages

import codecs                                                                               # used for encode and decode
import matplotlib.pyplot as plt                                                             # for ploting
import numpy as np                                                                          # for mathmatical functions
import pandas as pd                                                                         # for dataframe
import seaborn as sns                                                                       # for ploting
import seawater as sw                                                                       # calculating depth
import csv

df = pd.read_csv("/home/sahed/Desktop/office/1.meanData_mn_towed.txt", "\t")
#print(df)
#quit()

haul_id = df["haul"].str.split("_", expand = True)[1]                               # split haul to get rid "-"
df["haul"]=haul_id
haul_id_1 = df["haul"].str.split(".", expand = True)[0]                             # get rid of ".text"
df["haul"]=haul_id_1

data = {"haul": ["mn01", "mn02", "mn03", "mn04", "mn05", "mn06", "mn07",\
                  "mn08", "mn09", "mn10", "mn11", "mn12", "mn13", "mn14", "mn15", "mn16"],\
        "D_N": ["D", "N", "D", "N", "N", "D", "N", "D", "N", "D", "D", "N", "D",\
                "N", "D", "N"]}                                                            # dict for day and night hauls

DN_df=pd.DataFrame.from_dict(data)                                                         # dict to column in dataframe
df=pd.merge(df, DN_df, how="left", on="haul")                                 # merging two dataframe

data2 = {"haul": ["mn01", "mn02", "mn03", "mn04", "mn05", "mn06", "mn07",\
                  "mn08", "mn09", "mn10", "mn11", "mn12", "mn13", "mn14", "mn15", "mn16"],\
         "latitude": [-10.888, -10.951, -10.761, -10.778, -12.412, -12.414, -12.212, -12.212333,\
                      -14.001, -14.0015, -14.297, -14.277, -15.424, -15.430, -15.861, -15.860],\
         "longitude": [-78.5685, -78.564, -78.271, -78.270, -77.813, -77.812, -77.439, -77.439,\
                       -76.660, -76.660, -77.169, -77.177, -75.444, -75.44, -76.105, -76.106]}
lats_logs_df=pd.DataFrame.from_dict(data2)                                                    # dict to dataframe
df=pd.merge(df, lats_logs_df, on="haul", how="left")                             # merging dataframe

data = {"haul": ["mn01", "mn02", "mn03", "mn04", "mn05", "mn06", "mn07",\
                  "mn08", "mn09", "mn10", "mn11", "mn12", "mn13", "mn14", "mn15", "mn16"],\
        "station": ["station 1", "station 1","station 2","station 2", "station 3",\
                    "station 3","station 4", "station 4","station 6","station 6","station 5",\
                    "station 5", "station 8","station 8","station 7","station 7"]}
station=pd.DataFrame.from_dict(data)                                                       # dict to dataframe
df=pd.merge(df, station, on="haul", how="left")                              # merging the dataframes

df.to_csv("1. table for towed hauls.txt", sep="\t", encoding="utf-8")




