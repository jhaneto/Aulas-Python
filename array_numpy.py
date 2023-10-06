from numpy import *


vetor = array(eval(input("Informe o vetor: ")))

i = 0
count = 0

while(i < size(vetor)):
    if(vetor[i] == 5):
        count = count + 1
        print(i)
    i = i + 1
    
print(count)    