#include <iostream>
#include "slicing.h"
#include <Eigen/Core>
#include <Eigen/Geometry>
using namespace std;


CutNode generateCut(double a, double b, double c, double d)
{
  CutNode cn;
  cn.n[0] = a / sqrt(a*a + b*b + c*c);
  cn.n[1] = b / sqrt(a*a + b*b + c*c);
  cn.n[2] = c / sqrt(a*a + b*b + c*c);
  double p = d / sqrt(a*a + b*b + c*c);
  cn.pt[0] = cn.n[0] * p;
  cn.pt[1] = cn.n[1] * p;
  cn.pt[2] = cn.n[2] * p;
  return cn;
}


int main(int argc, char *argv[]) {
  cout << "im here\n";

  double z = 0;
  for(double x = -1; x <= 1; x += 0.2) {
    for(double y = -(sqrt(1 - x*x)); y <= sqrt(1 - x*x); y += 0.2) {
      for(double l = 0; l < 110; l += 10) {
        cout << "in loop\n";
        z = 1 - x*x - y*y;
        CutNode cn = generateCut(x, y, z, l);
        cout << " x= " <<  x << " y = " << y << " z = " << z << " l = " << l << " cost = " << slice(&cn, "Colonel.obj") << "\n";
      }
    }
  }
}

