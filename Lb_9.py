import numpy as np
import math
from math import factorial
from numpy import*
import matplotlib.pyplot as plt
x = np.array ([0.15, 0.16, 0.17, 0.18, 0.19, 0.20, 0.21, 0.22, 0.23, 0.24, 0.25])
y = np.array([4.4817, 4.9530, 5.4739, 6.0496, 6.6859, 7.3891, 8.1662, 9.0250, 9.9742, 11.0232, 12.1825])
x1=0.159
x2 = 0.234
h = x[1] - x[0]
q = (x1 - 0)/h
q1 = (x2 - 1)/h

def func( y, j):
    mas = []
    for i in range(len(y)):
        mas.append(y[i]-y[i-1])
    mas.pop(0)
    if j==1:
        return mas
    else:
        j -=1
        return func(mas,j)

   
yx1= y[0] - q1*(func(y, 1)[0]) + (q1*(q1-1)/factorial(2))*(func(y, 2)[0]) +  (q1*(q1-1)*(q1-2)/factorial(3))*(func(y, 3)[0])+(q1*(q1-1)*(q1-2)*(q1-4)/factorial(4))*(func(y, 4)[0])+(q1*(q1-1)*(q1-2)*(q1-3)*(q1-4)/factorial(5))*(func(y, 5)[0])
yx2= y[5] - q*(func(y, 1)[4]) + (q*(q-1)/factorial(2))*(func(y, 2)[3]) +  (q*(q-1)*(q-2)/factorial(3))*(func(y, 3)[2])+(q*(q-1)*(q-2)*(q-4)/factorial(4))*(func(y, 4)[1])+(q*(q-1)*(q-2)*(q-3)*(q-4)/factorial(5))*(func(y, 5)[0])
print(func(y, 1))

print("f()':", yx1)
print("f()'':",yx2)
plt.plot(x, y,'o',linestyle='-')
plt.grid()
plt.show()
	