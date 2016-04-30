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
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm


def two_d_array():
    return [random.uniform(-1, 1), random.uniform(-1, 1)]

a = []
b = []
cost = []
unseen_a = []
unseen_b = []
unseen_cost = []

with open(sys.argv[1]) as fn:
    for line in fn:
        cols = line.split()
        if len(cols) > 1:
            a.append(float(cols[0]))
            b.append(float(cols[1]))
            cost.append(float(cols[4]))


with open(sys.argv[2]) as fn:
    for line in fn:
        cols = line.split()
        if len(cols) > 1:
            unseen_a.append(float(cols[0]))
            unseen_b.append(float(cols[1]))
            unseen_cost.append(float(cols[4]))


rbfi = Rbf(a, b, cost, epsilon=0.1, smooth=1, function="multiquadric")
train(two_d_array, rbfi)

xs = np.linspace(min(a), max(a), 100)
ys = np.linspace(min(a), max(a), 100)
xs, ys = np.meshgrid(xs, ys)
fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")
ax.plot_wireframe(xs, ys, rbfi(xs, ys), rstride=3, cstride=3, linewidth=0.5, color="r")
ax.set_xlabel("a")
ax.set_ylabel("b")
ax.scatter(a, b, zs=cost, s=50, c="black")
ax.scatter(unseen_a, unseen_b, zs=unseen_cost, s=50, c="green")
plt.show()
