
# GEOMAR Helmholtz Centre for Ocean Research Kiel, Germany
# Project: SFB 754, March 2019
# Sahed Ahmed Palash, Research Assistant

# Mapping through geo-stations and create a plot
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

# load the file first and explore
mn_biomass = pd.read_csv("/home/sahed/Desktop/office/4. m138t_mn_midi_final_dataframe.txt", "\t")
print(mn_biomass.head())
print(mn_biomass.shape)
print(mn_biomass.info)
print(mn_biomass.describe())

# constructing the base map
map = Basemap(projection='merc', llcrnrlat=-17, urcrnrlat=-9, llcrnrlon=-80, urcrnrlon=-73, resolution="h")
map.drawmapboundary(fill_color='aqua')
map.fillcontinents(color='green', lake_color='blue')
map.drawcoastlines()
parallels = np.arange(-17., -09., 1.)
map.drawparallels(parallels, labels=[False, True, True, False])
meridians = np.arange(-79., -73., 1.)
map.drawmeridians(meridians, labels=[True, False, False, True])

# creating x and y coordinates for the map
lons = mn_biomass["longitude"].tolist()
lats = mn_biomass["latitude"].tolist()
a2, b2 = (-73, -9)
x, y = map(lons, lats)
map.scatter(x, y, marker='p', color='brown', s=100)
plt.title("Sampling Stations")

# creating coordinates for Peru and Lima
a, b = map(-75.8, -11.8)
c, d = map(-73.7, -10.5)
lat = -77.0428
lon = -12.0464
lat, lon = map(lat, lon)

# Mapping Lima
plt.annotate("Lima", xy=(a, b), xytext=(a2, b2), textcoords='offset points', color='yellow', fontsize=15)
map.plot(lat, lon,
         linestyle='none',
         marker="o",
         markersize=12,
         alpha=0.8,
         c="yellow",
         markeredgecolor="black",
         markeredgewidth=1)

# Mapping Peru
plt.annotate("Peru", xy=(c, d), xytext=(a2, b2), textcoords='offset points', color='yellow', fontsize=18)

# Mapping station names
e, f = map(-77.7, -10.65)
g, h = map(-77.15, -10.85)
i, j = map(-76.9, -12.15)
k, l = map(-76.4, -12.3)
m, n = map(-75.75, -14.15)
o, p = map(-76.27, -14.05)
q, r = map(-74.5, -15.6)
s, t = map(-75.15, -15.6)
plt.annotate("st1", xy=(e, f), xytext=(a2, b2), textcoords='offset points', color='black', fontsize=14)
plt.annotate("st2", xy=(g, h), xytext=(a2, b2), textcoords='offset points', color='black', fontsize=14)
plt.annotate("st3", xy=(i, j), xytext=(a2, b2), textcoords='offset points', color='black', fontsize=14)
plt.annotate("st4", xy=(k, l), xytext=(a2, b2), textcoords='offset points', color='black', fontsize=14)
plt.annotate("st6", xy=(m, n), xytext=(a2, b2), textcoords='offset points', color='black', fontsize=14)
plt.annotate("st5", xy=(o, p), xytext=(a2, b2), textcoords='offset points', color='black', fontsize=14)
plt.annotate("st8", xy=(q, r), xytext=(a2, b2), textcoords='offset points', color='black', fontsize=14)
plt.annotate("st7", xy=(s, t), xytext=(a2, b2), textcoords='offset points', color='black', fontsize=14)

plt.savefig("7.sampling_stations.png", dpi=300)
plt.show()