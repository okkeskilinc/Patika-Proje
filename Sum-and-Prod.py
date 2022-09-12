""""HackerRank Sum and Prod"""
import numpy as np

_shape=[int(i) for i in input().split()]
a=[input().split() for i in range(_shape[0])]
_a=np.array(a).astype(int)

print(np.prod(np.sum(_a,axis=0)))
