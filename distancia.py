# from math import *
# def distancia(lat1, lat2, lon1, lon2):
#     lon1 = radians(lon1)
#     lon2 = radians(lon2)
#     lat1 = radians(lat1)
#     lat2 = radians(lat2)
# 
#     # Haversine formula
#     dlon = lon2 - lon1
#     dlat = lat2 - lat1
#     a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
# 
#     c = 2 * asin(sqrt(a))
# 
#     # Radius of earth in kilometers. Use 3956 for miles
#     r = 6378.137
# 
#     # calculate the result
#     return(c * r)
#      
#      
# # driver code
# lat1 = 2.97185000
# lat2 = 60.01557778
# lon1 = 2.05998333
# lon2 =  60.01992778
# print(distancia(lat1, lat2, lon1, lon2), "K.M")
import math
 
# função que recebe dois pontos na terra e retorna a distância
# entre eles em quilômetros
def calcularDistancia(lat1, lat2, lon1, lon2):
  raio_terra = 6378.137 # raio da terra em quilômetros
     
  # o primeiro passo é converter as latitudes e longitudes
  # para radianos
  lon1 = math.radians(lon1)
  lon2 = math.radians(lon2)
  lat1 = math.radians(lat1)
  lat2 = math.radians(lat2)
  
  # agora aplicamos a Fórmula de Haversine
  dlon = lon2 - lon1
  dlat = lat2 - lat1
  a = math.pow(math.sin(dlat / 2), 2) + math.cos(lat1) * math.cos(lat2) \
    * math.pow(math.sin(dlon / 2),2)
              
  c = 2 * math.asin(math.sqrt(a))
  
  # e retorn__o_ _ ___tân___    
  return c
 
 
print(calcularDistancia(2.97185000,2.05998333, 60.01557778, 60.01992778))
