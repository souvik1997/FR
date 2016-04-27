from __future__ import print_function
import random
from deap import base
from deap import creator
from deap import tools
import subprocess
from find_minimum import train
#from rbf import Rbf
from scipy.interpolate import Rbf
import sys
import random
import numpy as np
import matplotlib.pyplot as plt


def one_d_array():
    return [random.uniform(-1, 1)]

a = []
cost = []

with open(sys.argv[1]) as fn:
    for line in fn:
        cols = line.split()
        if len(cols) > 1:
            a.append(float(cols[0]))
            cost.append(float(cols[1]))


rbfi = Rbf(a, cost, epsilon=0.1, smooth=0, function="gaussian")
train(one_d_array, rbfi)

x = np.linspace(min(a), max(a), 100)
plt.plot(x, rbfi(x))
plt.plot(a, cost, "o")
plt.show()