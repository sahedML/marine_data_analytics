
# GEOMAR Helmholtz Centre for Ocean Research Kiel, Germany
# Project: SFB 754, February 2019
# Sahed Ahmed Palash, Research Assistant

# create station-wise subset and plot them
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# load the integrated abundance file and explore
abundance = pd.read_csv("/home/sahed/Desktop/office/5.b.c. m138t_integrated_abundance_overall.txt", ",")
print(abundance.head())
print(abundance.shape)
print(abundance.info)
print(abundance.describe())

# creating station wise subset df
st1 = abundance["station"] == "Station 1"
st1 = abundance[st1]
st1 = st1.reset_index()

st2 = abundance["station"] == "Station 2"
st2 = abundance[st2]
st2 = st2.reset_index()

st3 = abundance["station"] == "Station 3"
st3 = abundance[st3]
st3 = st3.reset_index()

st4 = abundance["station"] == "Station 4"
st4 = abundance[st4]
st4 = st4.reset_index()

st5 = abundance["station"] == "Station 5"
st5 = abundance[st5]
st5 = st5.reset_index()

st6 = abundance["station"] == "Station 6"
st6 = abundance[st6]
st6 = st6.reset_index()

st7 = abundance["station"] == "Station 7"
st7 = abundance[st7]
st7 = st7.reset_index()

st8 = abundance["station"] == "Station 8"
st8 = abundance[st8]
st8 = st8.reset_index()

# creating station wise boxplot
fig = plt.figure(figsize=[8, 10])

fig1 = fig.add_axes([0.1, 0.79, 0.38, 0.15])
sns.stripplot(x="cat_short", y="integrated_abundance", data=st1, size=12, linewidth=1.5,   hue="D_N")
plt.title("Station 1 ", size=9)
sns.despine(left=False, bottom=False, right=True)
plt.xlabel("Category", size=9)
plt.ylabel("Individuals m⁻²", size=9)
plt.ylim(-5000, 51000)
plt.yticks(np.arange(0, 51000, 10000))
plt.legend(loc='upper right', fontsize=8)

fig2 = fig.add_axes([0.58, 0.79, 0.40, 0.15])
sns.stripplot(x="cat_short", y="integrated_abundance", data=st2, size=12, linewidth=1.5,   hue="D_N")
plt.title("Station 2 ", size=9)
sns.despine(left=False, bottom=False, right=True)
plt.xlabel("Category", size=9)
plt.ylabel("Individuals m⁻²", size=9)
plt.ylim(-5000, 51000)
plt.yticks(np.arange(0, 51000, 10000))
plt.legend(loc='upper right', fontsize=8)

fig3 = fig.add_axes([0.1, 0.56, 0.38, 0.16])
sns.stripplot(x="cat_short", y="integrated_abundance", data=st3, size=12, linewidth=1.5,   hue="D_N")
plt.title("Station 3 ", size=9)
sns.despine(left=False, bottom=False, right=True)
plt.xlabel("Category", size=9)
plt.ylabel("Individuals m⁻²", size=9)
plt.ylim(-5000, 51000)
plt.yticks(np.arange(0, 51000, 10000))
plt.legend(loc='upper right', fontsize=8)

fig4 = fig.add_axes([0.58, 0.56, 0.40, 0.16])
sns.stripplot(x="cat_short", y="integrated_abundance", data=st4, size=12, linewidth=1.5,   hue="D_N")
plt.title("Station 4 ", size=9)
sns.despine(left=False, bottom=False, right=True)
plt.xlabel("Category", size=9)
plt.ylabel("Individuals m⁻²", size=9)
plt.ylim(-5000, 51000)
plt.yticks(np.arange(0, 51000, 10000))
plt.legend(loc='upper right', fontsize=8)

fig5 = fig.add_axes([0.1, 0.31, 0.38, 0.18])
sns.stripplot(x="cat_short", y="integrated_abundance", data=st5, size=12, linewidth=1.5,   hue="D_N")
plt.title("Station 5 ", size=9)
sns.despine(left=False, bottom=False, right=True)
plt.xlabel("Category", size=9)
plt.ylabel("Individuals m⁻²", size=9)
plt.ylim(-1000, 15100)
plt.yticks(np.arange(0, 15100, 3000))
plt.legend(loc='upper right', fontsize=8)

fig6 = fig.add_axes([0.58, 0.31, 0.40, 0.18])
sns.stripplot(x="cat_short", y="integrated_abundance", data=st6, size=12, linewidth=1.5,   hue="D_N")
plt.title("Station 6 ", size=9)
sns.despine(left=False, bottom=False, right=True)
plt.xlabel("Category", size=9)
plt.ylabel("Individuals m⁻²", size=9)
plt.ylim(-1000, 15100)
plt.yticks(np.arange(0, 15100, 3000))
plt.legend(loc='upper right', fontsize=8)

fig7 = fig.add_axes([0.1, 0.06, 0.38, 0.17])
sns.stripplot(x="cat_short", y="integrated_abundance", data=st7, size=12, linewidth=1.5,   hue="D_N")
plt.title("Station 7 ", size=9)
sns.despine(left=False, bottom=False, right=True)
plt.xlabel("Category", size=9)
plt.ylabel("Individuals m⁻²", size=9)
plt.ylim(-8000, 126000)
plt.yticks(np.arange(0, 126000, 25000))
plt.legend(loc='upper right', fontsize=8)

fig8 = fig.add_axes([0.59, 0.06, 0.40, 0.17])
sns.stripplot(x="cat_short", y="integrated_abundance", data=st8, size=12, linewidth=1.5,   hue="D_N")
plt.title("Station 8 ", size=9)
sns.despine(left=False, bottom=False, right=True)
plt.xlabel("Category", size=9)
plt.ylabel("Individuals m⁻²", size=9)
plt.ylim(-8000, 126000)
plt.yticks(np.arange(0, 126000, 25000))
plt.legend(loc='upper right', fontsize=8)

plt.tight_layout()
plt.figtext(.2, .98, "Integrated Abundance Offshore")
plt.figtext(.68, .98, "Integrated Abundance Onshore")
plt.savefig('5.c. integrated_abundance_allStations.png', dpi=300)
plt.show()
