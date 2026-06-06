from numpy import *

A = array(1)
B = array([1,2,3])

C = array([[1,2,3],
          [1,2,3],
          [1,2,3]])

D = array([[[1,2,3],
            [1,2,3],
            [1,2,3]],
           
           [[1,2,3],
            [1,2,3],
            [1,2,3]],
            
           [[1,2,3],
            [1,2,3],
            [1,2,3]]])

S = [A, B, C, D]

for el in S[::-1]:
    print(el.ndim)
    print(el.shape)
