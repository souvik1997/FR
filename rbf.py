import scipy
from scipy.interpolate import Rbf
import sys
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
            d.append(float(cols[3])/100)
            cost.append(float(cols[4]))
            if len(a) > 10:
                rbfi = Rbf(a,b,c,d,cost)
                print rbfi(0.6, -0.6, 0.29, 10/100)
        count = count is False


rbfi = Rbf(a,b,c,d,cost)
print rbfi(0.6, -0.6, 0.29, 10/100)
