
# GEOMAR Helmholtz Centre for Ocean Research Kiel, Germany
# Project: SFB 754, March 2019
# Sahed Ahmed Palash, Research Assistant

# creating a map containing plankton biomass distribution in stations specified with geo-location
from mpl_toolkits.basemap import Basemap
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# load the file and explore
mn_biomass_df = pd.read_csv("/home/sahed/Desktop/office/4. m138t_mn_midi_final_dataframe.txt", "\t")
print(mn_biomass_df.head())
print(mn_biomass_df.shape)
print(mn_biomass_df.info)
print(mn_biomass_df.describe())

# function to convert integrated biomass from micro to milligram
fn = lambda row: row["integrated_biomass"]/1000
col = mn_biomass_df.apply(fn, axis=1)
mn_biomass_df = mn_biomass_df.assign(integrated_biomass_mili=col.values)

# create a dict for the stations with same multinet and merge with previous df
net_stations_dict = {
    "haul":
        ["mn01", "mn02", "mn03", "mn04",
         "mn05", "mn06", "mn07", "mn08",
         "mn09", "mn10", "mn11", "mn12",
         "mn13", "mn14", "mn15", "mn16"],

    "station":
        ["station 1", "station 1", "station 2", "station 2",
         "station 3", "station 3", "station 4", "station 4",
         "station 6", "station 6", "station 5", "station 5",
         "station 8", "station 8", "station 7", "station 7"]}

net_station_df = pd.DataFrame.from_dict(net_stations_dict)
mn_biomass_df = pd.merge(mn_biomass_df, net_station_df, on="haul", how="left")
mn_biomass_df = mn_biomass_df.groupby('station')["integrated_biomass_mili"].sum()

# creating station wise subset of df
st1 = mn_biomass_df["station"] == "station 1"
st1 = mn_biomass_df[st1]
st1 = st1.groupby("category")["integrated_biomass_mili"].sum()
st1 = st1.reset_index()

st2 = mn_biomass_df["station"] == "station 2"
st2 = mn_biomass_df[st2]
st2 = st2.groupby("category")["integrated_abundance"].sum()
st2 = st2.reset_index()

st3 = mn_biomass_df["station"] == "station 3"
st3 = mn_biomass_df[st3]
st3 = st3.groupby("category")["integrated_abundance"].sum()
st3 = st3.reset_index()

st4 = mn_biomass_df["station"] == "station 4"
st4 = mn_biomass_df[st4]
st4 = st4.groupby("category")["integrated_abundance"].sum()
st4 = st4.reset_index()

st5 = mn_biomass_df["station"] == "station 5"
st5 = mn_biomass_df[st5]
st5 = st5.groupby("category")["integrated_abundance"].sum()
st5 = st5.reset_index()

st6 = mn_biomass_df["station"] == "station 6"
st6 = mn_biomass_df[st6]
st6 = st6.groupby("category")["integrated_abundance"].sum()
st6 = st6.reset_index()

st7 = mn_biomass_df["station"] == "station 7"
st7 = mn_biomass_df[st7]
st7 = st7.groupby("category")["integrated_abundance"].sum()
st7 = st7.reset_index()

st8 = mn_biomass_df["station"] == "station 8"
st8 = mn_biomass_df[st8]
st8 = st8.groupby("category")["integrated_abundance"].sum()
st8 = st8.reset_index()

# constructing a basemap
map = Basemap(projection='merc', llcrnrlat=-17, urcrnrlat=-9, llcrnrlon=-80, urcrnrlon=-73, resolution='h')
map.drawmapboundary(fill_color='aqua')
map.fillcontinents(color='grey', lake_color='aqua')
map.drawcoastlines()
parallels = np.arange(-17., -09., 2.)
map.drawparallels(parallels, labels=[False, True, True, False])
meridians = np.arange(-79., -73., 2.)
map.drawmeridians(meridians, labels=[True, False, False, True])

# creating list of latitude, longitude and biomass

lats = [-10.888, -10.951, -10.761, -10.778,
        -12.412, -12.414, -12.212, -12.212333,
        -14.001, -14.0015, -14.297, -14.277,
        -15.424, -15.430, -15.861, -15.860]

lons = [-78.5685, -78.564, -78.271, -78.270,
        -77.813, -77.812, -77.439, -77.439,
        -76.660, -76.660, -77.169, -77.177,
        -75.444, -75.44, -76.105, -76.106]

biomass_list = mn_biomass_df["integrated_biomass"].tolist()

# creating a size fraction for the biomass with a factor,
# the quotient determine the size of plot visualization
factor = 200000
biomass = np.divide(biomass_list, factor)

# creating the map using tissot(representation of a circle on the map)
iterator = range(0, len(biomass_list))
for i in iterator:
    map.tissot(lons[i], lats[i], biomass[i], 20, edgecolor='k', facecolor='b', alpha=1)

# creating legends for biomass size fraction
fac_list = [0.3, 0.2, 0.1, 0.04]
lat_list = [-12, -12.7, -13.2, -13.6]
lon = -74
label_list = ["60000 µgCm⁻²", "40000 µgCm⁻²", "20000 µgCm⁻²", "8000 µgCm⁻²"]
for i in range(0, len(label_list)):
    map.tissot(-74.9, lat_list[i], fac_list[i], 20, edgecolor='k', facecolor='g', alpha=1)

# annotating the label list and text over the map
a, b = map(-73.4, -12)
c, d = map(-73.4, -12.6)
e, f = map(-73.4, -13.1)
g, h = map(-73.4, -13.5)
x, y = map(-75.4, -11.5)
a2, b2 = (-73, -9)
plt.annotate(label_list[0], xy=(a, b), xytext=(a2, b2), textcoords='offset points', color='black', fontsize=13)
plt.annotate(label_list[1], xy=(c, d), xytext=(a2, b2), textcoords='offset points', color='black', fontsize=12)
plt.annotate(label_list[2], xy=(e, f), xytext=(a2, b2), textcoords='offset points', color='black', fontsize=11)
plt.annotate(label_list[3], xy=(g, h), xytext=(a2, b2), textcoords='offset points', color='black', fontsize=10)
plt.annotate("Lima", xy=(x, y), xytext=(a2, b2), textcoords='offset points', color='yellow', fontsize=18)

# Mapping station names
i, j = map(-77.7, -11.1)
k, l = map(-77.3, -10.3)
m, n = map(-76.9, -12.6)
o, p = map(-76.5, -11.8)
q, r = map(-75.7, -13.5)
s, t = map(-76.3, -14.5)
u, v = map(-74.5, -15.2)
w, z = map(-75.2, -16)
plt.annotate("st1", xy=(i, j), xytext=(a2, b2), textcoords='offset points', color='black', fontsize=14)
plt.annotate("st2", xy=(k, l), xytext=(a2, b2), textcoords='offset points', color='black', fontsize=14)
plt.annotate("st3", xy=(m, n), xytext=(a2, b2), textcoords='offset points', color='black', fontsize=14)
plt.annotate("st4", xy=(o, p), xytext=(a2, b2), textcoords='offset points', color='black', fontsize=14)
plt.annotate("st6", xy=(q, r), xytext=(a2, b2), textcoords='offset points', color='black', fontsize=14)
plt.annotate("st5", xy=(s, t), xytext=(a2, b2), textcoords='offset points', color='black', fontsize=14)
plt.annotate("st8", xy=(u, v), xytext=(a2, b2), textcoords='offset points', color='black', fontsize=14)
plt.annotate("st7", xy=(w, z), xytext=(a2, b2), textcoords='offset points', color='black', fontsize=14)

plt.savefig("8. Biomass_distribution.png", dpi=300)
plt.show()
