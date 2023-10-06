
from decimal import Decimal

print(sum([Decimal('0.1')]*10) == Decimal('1.0'))
texto = ''
print('{:*^30}'.format(texto))

def somatorio(*args, **kwargs): # (4)
    resultado = 0
    chaves = sorted(kwargs.keys())
    for chave in chaves:
        print(chave, '=', kwargs[chave], ' ', end=''+'\n')
    for numero in args: # (5)
       resultado += numero
    return resultado 


print(somatorio(1,2,3,3,2,5, pessoa=10, povo=50))