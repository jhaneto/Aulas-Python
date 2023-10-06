# pintor = float(input('qual o preço? '))
# 
# 
# material =  float(input(' Entre com o Valor do Material '))
# b = float(input('Entre com o Comprimento '))
# h = float(input(' Entre com a Altura '))
# 
# area = b*h
# 
# total = area*pintor + material
# 
# print(total)
# from math import *
# 
# raio = float(input('Entre com o Raio '))
# 
# area = pi * raio ** 2
# volume = 4/3 * pi * raio ** 3
# 
# print(f'Area = {area}')
# print(f'Volume = {volume}')
# tracinho = ('-=')*30
# espaco = (' ')*4
# from math import *
# 
# linha  = ('-=')*30
# print(f'{linha} Entre com os Lados de um Triangulo {linha}')
# a = float(input('Entre com o Lado 1 '))
# b = float(input('Entre com o Lado 2 '))
# c = float(input('Entre com o Lado 3 '))
# 
# s = (a+b+c)/2
# 
# 
# area = sqrt(s * (s-a) * (s-b) * (s-c))
# 
# print(f'Valor da Area do triangulo = {area}')
from math import *

linha  = ('-=')*5
print(f'{linha} Entre com os Ponto Inicial {linha}')

lat1 = float(input('Entre com o Latitude Ponto Inicial '))
long1 = float(input('Entre com o Longitude Ponto Inicial '))

print(f'{linha} Entre com os Ponto Final {linha}')

lat2 = float(input('Entre com o Latitude Ponto Final '))
long2 = float(input('Entre com o Longitude Ponto Final '))

#Raio da terra
R = 6371.01

d = R * acos(sin(lat1) * sin(lat2) + cos(lat1) * cos(lat2) * cos(long1 - long2))

print(f'Adistancia é {round(d,2)} Km')
