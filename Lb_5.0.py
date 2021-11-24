import numpy as np
from numpy import linalg
def gggauss(a, b):
  c = np.linalg.inv(a)
  print('Ggauss')
  print(c*b)
  print('Solve', np.linalg.solve(a, b))
  
gggauss(np.matrix([[1, 2, -1], [3, 4, 1], [5, 1, -3]]), np.matrix([[-3], [1], [-2]]))