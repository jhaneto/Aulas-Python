vetor = [1,2,3,5,7,0,20,6]

from numpy import *

import matplotlib.pyplot as plt




f  =  poly1d([1,-10,15])
x = linspace(0,10,15)

y = polyval(f,x)

plt.figure()

plt.plot(x,y)
plt.ylim(-10,15)
plt.xlim(0,10)

plt.xlabel("x", fontsize='large')

plt.ylabel("y", fontsize='large')

plt.grid(True)
plt.show()

v = ones(10, dtype=int)

print(v)

plt.title("Exemplo Meu")