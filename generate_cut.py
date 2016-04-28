from __future__ import print_function
import sys
import math
def generateCut(a, b, c, d):
    c = math.sqrt(c)
    p = d / math.sqrt(a*a + b*b + c*c);
    n1 = a / math.sqrt(a*a + b*b + c*c)
    n2 = b / math.sqrt(a*a + b*b + c*c)
    n3 = c / math.sqrt(a*a + b*b + c*c)
    p1 = p * n1
    p2 = p * n2
    p3 = p * n3
    print("0 0 {0} {1} {2} {3} {4} {5}".format(p1, p2, p3, n1, n2, n3))


generateCut(float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3]), float(sys.argv[4]))
