import numpy as np
import math

masX = [2.4, 2.6, 2.8, 3.0, 3.2, 3.4, 3.6, 3.8, 4.0]
masY = [3.526, 3.782, 3.945, 4.043, 4.104, 4.155, 4.222, 4.331, 4.507]
h = masX[1] - masX[0]
Mas = []
Mas1 = []
Mas2 = []
Mas3 = []
for i in range(len(masX)):
  Mas.append(masY[i] - masY[i - 1])
Mas.pop(0)

for e in range(len(Mas)):
  Mas1.append(Mas[e] - Mas[e - 1])
Mas1.pop(0)

for u in range(len(Mas1)):
  Mas2.append(Mas1[u] - Mas1[u - 1])
Mas2.pop(0)

for o in range(len(Mas2)):
  Mas3.append(Mas2[o] - Mas2[o - 1])
Mas3.pop(0)

y1 = 1 / h * (Mas[1]  - (Mas1[1] / 2) + (Mas2[1] / 3) - (Mas3[1] / 4))
y2 = 1 / h**2 * (Mas1[1] - Mas2[1] + (11 / 12 * Mas3[1]))

print('First derivative = ', y1)
print('Second derivative = ', y2)