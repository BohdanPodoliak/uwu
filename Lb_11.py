import numpy as np
import matplotlib.pyplot as plt
import numpy as np
from math import cos

def f(x) :
   result = (-4*x**3)/3
   return result

x = np.linspace(0.0, 7.0, 100)
y = np.sin(2*x) -2*x
y2 = (-4*x**3)/3

plt.title("Метод Тейлора графика sin(2*x) -2*x")
plt.xlim(0, 7 + 0.2)
plt.ylim(-5, 5 + 1)
plt.plot(x, y, label='sin(2*x) -2*x')
plt.plot(x, y2, label='(-4*x**3)/3')
plt.legend()
plt.grid()
plt.show()
