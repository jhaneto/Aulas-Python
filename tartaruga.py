from turtle import Screen
from pista import Pista
from jogador import Jogador
from carros import CarroConfig
import time

tela  = Screen()

tela.setup(600,600)
tela.title('Tartaruga experta')
tela.tracer(0)
tela.bgcolor("lightgreen")  
tela.listen()
pista = Pista()
jogador = Jogador()
carro_config = CarroConfig()
tela.onkey(jogador.mover_direita, 'Right')
tela.onkey(jogador.mover_esquerda, 'Left')
jogo_on = True
while jogo_on== True:
    time.sleep(0.1)
    carro_config.aparecer_carro()
    carro_config.mover_carro()
    tela.update()

tela.exitonclick()