import matplotlib.pyplot as plt
from scipy.interpolate import UnivariateSpline
from numpy import *

x = [0.8, 1.2, 1.4, 1.7, 2.2]
y = [3.18, 2.15, 4.18, 3.81, 5.07]
plt.scatter(x, y, label = "Задані точки", color = "g")
plt.grid(True)
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Інтерполяція сплайнами")
spl = UnivariateSpline(x, y)
xs = linspace(-1, 4.5, 1000)
plt.plot(x, y, "go", xs, spl(xs), "m")
plt.legend(fontsize = 12, edgecolor = "black", facecolor = "red", loc = "lower left")
plt.show()
