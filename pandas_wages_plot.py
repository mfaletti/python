#!/usr/bin/python
import pandas as pd
import matplotlib.pyplot as plt
#%pylab inline
# Tell Pandas the data is tab delimited
data = pd.read_csv("./data/wages_hours.csv", sep = "\t")
# we only need the AGE and Rate column from the data
data2 = data[["AGE", "RATE"]]
print(data2)
# sort the age in ascending order to properly plot the graph
data_sorted = data2.sort_values(["AGE"])
# Pandas by default puts an index, so we have to replace that column that before plotting in a x vs y format
data_sorted.set_index("AGE", inplace=True)
data_sorted.plot()
plt.show()
