from turtle import Turtle

class Pista(Turtle):
    def __init__(self):
        super().__init__()
        self.pensize(4)
        self.penup()
        self.goto(150, -400)
        self.pendown()
        self.goto(150,400)
        
        # segunda Linha
        
        self.desenhar_traco((90, -400))
        self.desenhar_traco((-90, -400))
        
        # terceira Linha
        
        self.desenhar_traco((30, -400))
        self.desenhar_traco((-30, -400))
        
        # Linha Final
        
        self.pensize(4)
        self.penup()
        self.goto(-150, -400)
        self.pendown()
        self.goto(-150,400)
    def desenhar_traco(self, pos):
         self.setheading(90)
         self.penup()
         self.goto(pos)
         for traco in range(30):
             self.forward(20)
             self.penup()
             self.forward(20)
             self.pendown()