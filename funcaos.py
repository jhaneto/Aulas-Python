def somar(num, num2):
    return num + num2

def diminuir(num, num2):
    return num - num2

def multiplicar(num, num2):
    return num * num2

def dividir(num, num2):
    return num / num2



def calcular(num, num2, funcao):
    return funcao(num, num2)


print(calcular(4, 2, somar))

print(calcular(4, 2, diminuir))
   
print(calcular(4, 2, multiplicar))

print(calcular(4, 2, dividir))

from random import choice

def cumprimento(pessoa):
    def humor():
        return choice(('E Ai ', 'Diz que nao estou ', 'Tudo Bem '))
    return humor() + pessoa

print(cumprimento('Marcos'))
print(cumprimento('Maria'))

def faz_me_rir():
    def rir():
        return choice(('haha', 'kkkk','uiui'))
    return rir

rindo = faz_me_rir()
print(rindo())
      
     
      
      
      
      