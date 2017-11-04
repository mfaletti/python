#!/usr/bin/python
import numpy as np
import matplotlib.pyplot as plt

salary = np.fromfile("./txt/salaries.txt", dtype=int, sep=",")
names = np.genfromtxt("./txt/names.txt", dtype='str', delimiter=",")

# x axis has to be a number, so create a variable x that will contain numbers for each name.
# The numpy arange generates a list of numbers starting from 0.
x = np.arange(len(names))

# plot x vs salary
plt.bar(x, salary)

# All it does it is replace the numbers in x with names. Because we can only plot against numbers, 
# we had to use this round the way approach.
plt.xticks(x, names)

plt.ylabel("Salaries")
plt.xlabel("Names")
plt.title("Salary of 10 random people")
plt.show()

# print some basic stats
print(np.max(salary), np.min(salary), np.average(salary), np.median(salary))
