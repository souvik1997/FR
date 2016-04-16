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


int main(int argc, char *argv[])
{
  CutNode cn = generateCut(1,1,1,1);
  cout << cn.n << "\n" << cn.pt << "\n";
  cout << slice(&cn, "Colonel.obj") << "\n";
  return 0;
}
