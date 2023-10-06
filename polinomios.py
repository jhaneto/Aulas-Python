from numpy import *

vetor = array(eval(input("Coeficientes : ")))

Z = int(input("Ponto Z: "))

f = poly1d(vetor)


raizes = roots(f)

print(f"A(s) raiz(es) : {raizes} ") 

result = polyval(f,Z)

print(f"Polinomios no Ponto Z: {result}")