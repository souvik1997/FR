#include <Eigen/Core>
#include <Eigen/Geometry>

struct CutNode
{

CutNode() : lchild(NULL), rchild(NULL) {}
  ~CutNode() {delete lchild; delete rchild;}

  Eigen::Vector3d pt;
  Eigen::Vector3d n;
  CutNode *lchild, *rchild;
};

struct LineInfo
{
  int lchild;
  int rchild;
  Eigen::Vector3d pt;
  Eigen::Vector3d n;
};
int slice(CutNode* cuttree, std::string filename);
