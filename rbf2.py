from __future__ import print_function
import scipy
from rbf import Rbf
#from scipy.interpolate import Rbf
import sys
import math
import numpy as np
a = []
b = []
c = []
d = []
cost = []
with open(sys.argv[1]) as fn:
    for line in fn:
        cols = line.split()
        if len(cols) > 4 and np.random.randint(0,1) == 0:
            a.append(float(cols[0]))
            b.append(float(cols[1]))
            c.append(math.sqrt(abs(float(cols[2]))))
            d.append(float(cols[3]))
            cost.append(float(cols[4]))
rbfi = Rbf(a, b, c, d, cost, epsilon=0.1, smooth=-1)
ctr = 0
for ctr in xrange(0, 901):
    print((a[ctr], b[ctr], c[ctr], d[ctr], rbfi(a[ctr], b[ctr], c[ctr], d[ctr]), cost[ctr]))
