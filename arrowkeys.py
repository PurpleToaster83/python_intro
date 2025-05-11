import turtle
import random
from turtle import *

draw = turtle.Turtle()
draw.speed(0)
draw.width(2)
draw.shape('turtle')

colors = ['red', 'blue', 'green', 'yellow', 'purple', 'orange', 'black']

def up():
    draw.setheading(90)
    draw.forward(100)
    
def down():
    draw.setheading(270)
    draw.forward(100)
    
def left():
    draw.setheading(180)
    draw.forward(100)
 
def right():
    draw.setheading(0)
    draw.forward(100)

def clickleft(x,y):
    draw.color(random.choice(colors))

def spacebar():
    draw.stamp()

turtle.listen()

turtle.onscreenclick(clickleft, 1)

turtle.onkey(spacebar, 'space')
turtle.onkey(up, 'Up')
turtle.onkey(down, 'Down')
turtle.onkey(left, 'Left')
turtle.onkey(right, 'Right')
   
turtle.mainloop()
