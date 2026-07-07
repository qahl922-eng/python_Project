# This is Our Python File for Practicing different Concepts and Method/Function of Numpy.

import array as ar
import numpy as np

A = ar.array('i', [1,2,3,4,5,6])
print(A)
print(A.typecode)
A.reverse()
print(A)
A.reverse()

A.insert(1, 4)
# print(A)
# A.pop(1)
# print(A)
# A.remove(3)
# print(A)
# print(A.index(4))

# B = ar.array('f', [el for el in A])
# print(B)
# C = ar.array('f', (i for i in B))
# print(C)

BB = np.array([1,2,3,8,9,99,])
# print(BB, BB.dtype)

# C = np.array([1,2,3,4,'gh'])
# print(C)

# print(np.linspace(0, 20, 10, endpoint=False, retstep=True ))


# print(np.arange(2, 10, ))

# print(np.zeros(5))
# print(np.ones(5))
# print(np.full(5, 9))

# print(BB * 2)   # Vectorization

NP_1D = np.array([1,2,3,4,5,6])

NP_2D = np.array([[[1,2,3,4],
                  [3,3,3,3]],

                  [[1,6,0,5],
                   [11,12,14,15]]])

# print(NP_2D.ndim)
# print(NP_2D.shape)

NP_3D = np.array([[[1,2,3,4],
                   [3,3,3,3]],

                [[9,9,9,9],
                 [0,0,0,0]]])

# print(NP_3D.ndim)
# print(NP_3D.shape)

print(NP_3D[:, :, 0])

print(np.concatenate([NP_2D, NP_3D], axis=2))

