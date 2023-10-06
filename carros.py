from turtle import Turtle
import random

class CarroConfig:
    def __init__(self):
        self.carros = []
        self.local = [(0,100), (60,100), (120,100),(-60,100), (-120)]
        self.criar_carro()
    def criar_carro(self):
        random_number = random.randint(1,10)
        if random_number == 1:
            novo_carro = Turtle()
            cores = ['brown', 'red', 'black', 'cyan', 'grey', 'green', 'yellow', 'purple' ]
            novo_carro.penup()
            novo_carro.shape('square')
            novo_carro.setheading(270)
            novo_carro.shapesize(2.5, 4)
            
            novo_carro.color(random.choice(cores))
            novo_carro.goto(random.choice(self.local))
            self.carros.append(novo_carro)
        
    def aparecer_carro(self):
        if self.carros[-1].ycor() <= 20:
           self.criar_carro()
    
    def mover_carro(self):
         for carro in self.carros:
             carro.forward(5)