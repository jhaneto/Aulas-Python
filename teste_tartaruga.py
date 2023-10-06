from turtle import Turtle
from random import random
import turtle as t

# for i in range(100):
#     steps = int(random() * 100)
#     angle = int(random() * 360)
#     t.right(angle)
#     t.fd(steps)

# t = Turtle()
# for i in range(100):
#     steps = int(random() * 100)
#     angle = int(random() * 360)
#     t.right(angle)
#     t.fd(steps)
# 
# t.screen.mainloop()
# for steps in range(100):
#     for c in ('blue', 'red', 'green'):
#         t.color(c)
#         t.forward(steps)
#         t.right(30)
# 
# while True:
#     t.forward(200)
#     t.left(170)
#     if abs(t.pos()) < 1:
#         break

# for i in range(100):
#     steps = int(random() * 100)
#     angle = int(random() * 360)
#     t.right(angle)
#     t.fd(steps)

def draw_dream():
    window = t.Screen()
    window.bgcolor("white")
    window.exitonclick()
    
def draw_arm(brad):
    brad.forward(60)
    brad.left(60)
    brad.forward(60)
 
    brad.backward(60)
    brad.right(60)
    brad.backward(60)
 
    brad.right(60)
 
    brad.forward(60)
    brad.right(60)
    brad.forward(60)
 
    brad.backward(60)
    brad.left(60)
    brad.forward(90)
    
draw_dream() 