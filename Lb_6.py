import math
from scipy import optimize

x0 = -1.1
y0 = -1

def f1(y):
    return -2 + math.cos(y + 0.5)
    
def f2(x):
    return 1/2 * math.sin(x)/2

def iter(x, y, e):
    xn = x
    yn = y
    xn1 = f2(x)
    yn1 = f1(y)
    n = 1
    while((abs(xn1 - xn) >= e) & (abs(yn1-yn) >= e)):
        xn = xn1
        yn = yn1
        xn1 = f2(yn)
        yn1 = f1(xn1)
        n = n + 1
    print("Simple iteration:")
    print("x1 = ", xn, "\ny1 =", yn1,"\nThe amount of iteration = :", n)

iter(x0, y0, 0.0001)
    
def f3(x):
    return math.cos(x[1] + 0.5) - x[0] - 2, math.sin(x[0]) - 2 * x[1] - 1

s = optimize.root(f3, [0, 0], method = 'hybr')
print(s.x)