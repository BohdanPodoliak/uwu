from numpy import *
import matplotlib.pyplot as plt

def function(x):
    return sin(x)*(1/x)*cos(x**2+1/x)
    
x = linspace(-2, 2)
y = function(x)
plt.plot(x, y, 'b-', label='sin(x)*(1/x)*cos(x**2+1/x)')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()