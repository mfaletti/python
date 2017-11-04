#!/usr/bin/python
import pandas as pd
import matplotlib.pyplot as plt
#%pylab inline
data = pd.read_csv("./data/hubble_data.csv")
# Pandas by default puts an index, so we have to replace that column that before plotting in a x vs y format
data.set_index("distance", inplace=True)
data.plot()
plt.show()