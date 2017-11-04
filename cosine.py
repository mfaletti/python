#! /usr/bin/python
import numpy as np
import matplotlib.pyplot as plt

# create x, evenly spaced floating point numbers between 0-20
x = np.linspace(0,20,1000)
y1 = np.sin(x)
y2 = np.cos(x)

# plot the sin and cos functions
plt.plot(x, y1, "-g", label="sine")
plt.plot(x, y2, "-b", label="cos")

# The legend should be in the top right corner
plt.legend(loc="upper right")

# limit the y axis to -1.5 to 1.5 and show the plot
plt.ylim(-1.5, 1.5)
plt.show()