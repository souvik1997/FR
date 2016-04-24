from __future__ import print_function
import scipy
from scipy.interpolate import Rbf
import sys
import math
a = []
b = []
c = []
d = []
cost = []
count = True
with open(sys.argv[1]) as fn:
    for line in fn:
        cols = line.split(" ")
        if len(cols) == 5 and count is False:
            a.append(float(cols[0]))
            b.append(float(cols[1]))
            c.append(float(cols[2]))
            d.append(float(cols[3]))
            cost.append(float(cols[4]))
        count = count is False
def frange(start, end=None, inc=None):
    "A range function, that does accept float increments..."

    if end == None:
        end = start + 0.0
        start = 0.0

    if inc == None:
        inc = 1.0

    L = []
    while 1:
        next = start + len(L) * inc
        if inc > 0 and next >= end:
            break
        elif inc < 0 and next <= end:
            break
        L.append(next)

    return L

rbfi = Rbf(a,b,c,d,cost, smooth=0.5)
minimum = (0, 0, 0, 0, 1000000)
for x in set(a):
    for y in frange(-math.sqrt(1-x**2), math.sqrt(1-x**2), 0.2):
        for l in set(d):
            z = 1- x**2 - y**2
            val = rbfi(x,y,z,l)
            print("{0} {1} {2} {3} {4}".format(x,y,z,l, val))
            if val < minimum[4]:
                minimum = (x, y, z, l, val)
print(minimum)
