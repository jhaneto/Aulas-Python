from numpy import *


x = array(eval(input("Vetor das Abscissas: " )))


y = array(eval(input("Vetor das Ordenadas: ")))


i = 0
area = 0


while(i < size(x) - 2):
    area = (x[i+1] + x[i]) * (y[i+1] - y[i]) + area
    i = i + 1
    
area = abs(area) * 1/2.

print(round(area, 4))

