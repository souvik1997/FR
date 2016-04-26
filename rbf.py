from __future__ import printfn
import numpy as np
from scipy import linalg

class Rbf:

    def __init__(self, *args, **kwargs):
        self.inputs = []
        for x in args[:-1]:
            self.inputs.append(np.asarray(x, dtype=np.float_))
        self.inputs = np.asarray(self.inputs)
        self.num_inputs = len(args[0])
        self.expected_outputs = np.asarray(args[-1])

        raw_matrix = self.norm(self.inputs, self.inputs)
        self.epsilon = kwargs.pop('epsilon')
        self.smooth = kwargs.pop('smooth')

        self.fn = lambda r: np.exp(-(1.0/self.epsilon*r)**2)
        self.rbf_matrix = self.fn(raw_matrix) - np.eye(self.num_inputs)*self.smooth

        self.nodes = linalg.solve(self.rbf_matrix, self.expected_outputs)


    def __call__(self, *args):
        np_args = []
        for i in args:
            np_args.append(np.asarray(i).flatten())
        cur_inputs = np.asarray(np_args, dtype=np.float_)
        distances = self.norm(cur_inputs, self.inputs)
        return np.dot(self.fn(distances), self.nodes)[0]


    def norm(self, a, b):
        a = self.tranpose(a)
        b = self.fix_shape(b)
        return np.sqrt(((a - b)**2).sum(axis=0))

    def fix_shape(self, a):
        res = []
        for i in a:
            res.append([i])
        return np.asarray(res)

    def tranpose(self, a):
        a_transpose = []
        if len(a.shape) == 1:
            for i in a:
                a_transpose.append([i])
        else:
            for i in a:
                a_transpose.append(self.tranpose(i))
        return np.asarray(a_transpose)
