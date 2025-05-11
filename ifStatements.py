#William Van Uitert
#9/13/2023
#The purpose of this program is to demonstrate the use of if, elif, and else conditional statments

import turtle
import random
from turtle import *

draw = turtle.Turtle()
face = turtle.Turtle()
eyes = turtle.Turtle()
mouth = turtle.Turtle()

face.speed(12)
eyes.speed(10)
mouth.speed(10)

print("Choices are: flower, smiley face, or free-draw.")
choice = input("What would you like to draw?")

if(choice == "flower"):
    draw.speed(20)
    draw.color("pink")
    draw.penup()
    draw.setpos(0, -180)
    draw.pendown()
    draw.circle(180)

    face.color("white")
    eyes.color("white")
    mouth.color("white")

    draw.penup()
    draw.setpos(0,0)
    draw.pendown()
    for petal in range(24):
        draw.circle(100)
        draw.left(15)
elif(choice == "smiley face"):
    face.speed(12)
    eyes.speed(10)
    mouth.speed(10)

    draw.color("yellow")
    
    def smileyFace(smiley_x, smiley_y, smiley_size):
        face.color("yellow")
        eyes.color("black")
        mouth.color("yellow")

        face.penup()
        face.setpos(smiley_x, smiley_y)
        face.pendown()
        face.begin_fill()
        face.circle(smiley_size)
        face.end_fill()
        face.penup()
        face.setpos(smiley_x, smiley_y + (smiley_size * 0.5))
        
        def eye(side):
            eyes.penup()
            eyes.setpos(smiley_x + (side * (smiley_size * 0.5)), smiley_y + (smiley_size * 1.25))
            eyes.pendown()
            eyes.begin_fill()
            eyes.circle((3/20)*smiley_size)
            eyes.end_fill()
            eyes.penup()
            eyes.setpos(smiley_x, smiley_y)
            
        eye(1)
        
        eye(-1)

        eyes.penup()
        eyes.setpos(smiley_x, smiley_y + (smiley_size * 0.5))
        eyes.color("yellow")

        mouth.penup()
        mouth.setpos(smiley_x, smiley_y + (smiley_size * 0.35))
        mouth.pendown()
        mouth.color("black")
        mouth.begin_fill()
        mouth.circle(smiley_size * 0.5, 90)
        mouth.circle(-1 * ((1/20) * smiley_size), 180)
        mouth.circle(-1 * (smiley_size * (3/5)), 180)
        mouth.circle(-1 * ((1/20) * smiley_size), 180)
        mouth.circle(smiley_size * 0.5, 90)
        mouth.end_fill()
        mouth.penup()
        mouth.color("yellow")
        mouth.setpos(smiley_x, smiley_y + (smiley_size * 0.5))


    smileyFace(0, -125, 200)


else:
    draw.width(2)
    draw.shape('turtle')

    face.color("white")
    eyes.color("white")
    mouth.color("white")
    
    colors = ['red', 'blue', 'green', 'yellow', 'purple', 'orange', 'black']

    print("Hit space bar to stamp")
    print("Hit trackpad to change color")
    print("Use the arrow keys to move the turtle")

    def up():
        draw.setheading(90)
        draw.forward(80)
        
    def down():
        draw.setheading(270)
        draw.forward(80)
        
    def left():
        draw.setheading(180)
        draw.forward(80)
     
    def right():
        draw.setheading(0)
        draw.forward(80)

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
