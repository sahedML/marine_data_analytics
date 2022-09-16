
# GEOMAR Helmholtz Centre for Ocean Research Kiel, Germany
# Project: SFB 754, April 2019
# Sahed Ahmed Palash, Research Assistant

# calculate mean values and create a dataframe
import codecs
import matplotlib.pyplot as plt
import pandas as pd
import seawater as sw

# creating a dictionary of multinet ctd and cruise ctd with all other relevant information
dict = {
    "m138_mn01.txt": ["met_138_1_011.ctd", "-10.888"],
    "m138_mn02.txt": ["met_138_1_013.ctd", "-10.951"],
    "m138_mn03.txt": ["met_138_1_014.ctd", "-10.761"],
    "m138_mn04.txt": ["met_138_1_017.ctd", "-10.778"],
    "m138_mn06.txt": ["met_138_1_041.ctd", "-12.414"],
    "m138_mn05.txt": ["met_138_1_038.ctd", "-12.412"],
    "m138_mn08.txt": ["met_138_1_051.ctd", "-12.212"],
    "m138_mn07.txt": ["met_138_1_049.ctd", "-12.212"],
    "m138_mn11.txt": ["met_138_1_060.ctd", "-14.001"],
    "m138_mn12.txt": ["met_138_1_064.ctd", "-14.001"],
    "m138_mn13.txt": ["met_138_1_068.ctd", "-14.297"],
    "m138_mn14.txt": ["met_138_1_071.ctd", "-14.278"],
    "m138_mn15.txt": ["met_138_1_074.ctd", "-15.425"],
    "m138_mn16.txt": ["met_138_1_078.ctd", "-15.430"],
    "m138_mn17.txt": ["met_138_1_086.ctd", "-15.861"],
    "m138_mn18.txt": ["met_138_1_090.ctd", "-15.861"]
}

# calling a binary variable outside loop
data_frame_exist = 0

# calling a figure outside loop to create a plot for all the files together
fig = plt.figure(figsize=[7, 10])

# mapping through each file in the directory according to dict
for mn_filename in dict:
    ctd_filename_list = dict[mn_filename][0]
    lat = dict[mn_filename][1]

    # creating empty list to extract mean values from all the files
    mn_pressure = []
    mn_o2 = []
    mn_net = []
    mn_index = []
    mn_haul = []
    mn_volume = []
    mn_salinity = []
    mn_temp = []
    mn_depth = []

    # load all the multinet (mn) ctd files
    mn_upcast = codecs.open("/home/sahed/Desktop/office/mn_ctd/" + mn_filename,
                          "r", encoding="utf-8", errors="ignore")
    line_counter = 0
    xyz = 0

    # play with the file structure and clean a bit
    for line in mn_upcast:
        if xyz == 0:
            if "Time [hh:mm:ss]" in line:
                xyz = 1
                continue
        else:
            element_list_1 = line.strip().split("\t")
            if len(element_list_1) == 1:
                continue
            elif len(element_list_1) == 15:
                m = (float(element_list_1[2]))
                net = int(element_list_1[1])
                if m <= 150 and net >= 1:
                    mn_pressure.append(m)
                    o2_mlL = float(element_list_1[-2])
                    sw_density = float(element_list_1[-5])
                    mol_volume_o2 = 22.392
                    mn_o2.append(((o2_mlL/sw_density/1000/mol_volume_o2*1000)*1000000) - 10)
                    # o2 conversion mg to µmol (subtracting 10 for o2 calibration)
                    mn_net.append(net)
                    mn_index.append(net)
                    mn_haul.append(mn_filename)
                    volume = float(element_list_1[3])
                    mn_volume.append(volume)
                    mn_salinity.append(float(element_list_1[9]))
                    mn_temp.append(float(element_list_1[7]))
                    depth = sw.dpth(m, float(lat))
                    mn_depth.append(depth)

        line_counter += 1

    # creating a dataframe with mean values of some specific variables
    mn_dataframe = pd.DataFrame(
        {
        "haul": mn_haul,
        "net": mn_net,
        "depth": mn_depth,
        "o2": mn_o2,
        "salinity": mn_salinity,
        "temp": mn_temp
        }
    )

    # get rid of negative values
    mn_dataframe.loc[mn_dataframe['o2'] < 0, 'o2'] = 0

    # creating columns net opening, net closing and delta value
    mn_data_min = mn_dataframe.groupby(["haul", "net", ]).min()
    mn_net_closing = (mn_data_min["depth"])
    mn_net_closing.name = "net_closing"
    mn_data_max = mn_dataframe.groupby(["haul", "net", ]).max()
    mn_net_opening = (mn_data_max["depth"])
    mn_net_opening.name = "net_opening"

    # joining net opening and net closing
    net_df = pd.concat([mn_net_opening, mn_net_closing], axis=1)
    net_df = net_df.reset_index()

    # merging net_df on mn_dataframe
    mn_dataframe = mn_dataframe.merge(net_df, on=["haul", "net"], how="inner")

    # creating a column with delta values by subtracting the net opening and closing values
    fn = lambda row: row["net_opening"] - row["net_closing"]
    col = mn_dataframe.apply(fn, axis=1)
    mn_dataframe = mn_dataframe.assign(delta_values=col.values)

    # creating dataframe grouped with mean value
    mn_data_grouped = mn_dataframe.groupby(["haul", "net"]).mean()
    mn_data_grouped.reset_index()

    # appending the each multinet files
    if data_frame_exist == 0:
        final_df = mn_data_grouped
        data_frame_exist = 1

    else:
        final_df = final_df.append(mn_data_grouped)

# saving the file
final_df.to_csv("11.meanData_mn_vertical.txt", sep='\t', encoding='utf-8')
