#William Van Uitert
#09/04/2023
#The purpose of this program is to show competancy in using for loops and using turtle libraries to draw

import turtle

red = turtle.Turtle()
blue = turtle.Turtle()
purple = turtle.Turtle()
red.speed(50)
blue.speed(50)
purple.speed(10)


#W    
purple.color("white")
purple.right(90)
purple.forward(300)
purple.right(90)
purple.forward(100)
purple.right(75)
purple.color("purple")
purple.forward(100)
purple.left(180)
purple.forward(100)
purple.left(140)
purple.forward(90)
purple.right(130)
purple.forward(90)
purple.left(140)
purple.forward(100)

#I
purple.color("white")
purple.right(165)
purple.forward(110)
purple.left(90)
purple.forward(20)
purple.left(90)
purple.color("purple")
purple.forward(80)
purple.color("white")
purple.forward(10)
purple.right(90)
purple.forward(1)
purple.color("purple")
purple.begin_fill()
purple.circle(3)
purple.end_fill()

#L
purple.color("white")
def l():
    purple.right(90)
    purple.forward(90)
    purple.color("white")
    purple.left(90)
    purple.forward(20)
    purple.left(90)
    purple.color("purple")
    purple.forward(100)
    
l()

#L
purple.color("white")
purple.right(180)
purple.forward(10)
purple.left(90)
purple.color("purple")
l()

purple.color("white")

red.color("white")
blue.color("white")

red.left(90)
blue.left(90)

red.forward(50)
blue.forward(50)

red.right(90)
blue.right(90)

red.color("red")
blue.color("blue")

for angle in range(72):
    red.left(5)
    
    for side in range(4):
        red.forward(160)
        red.left(90)
        
blue.right(2.5)

for angle in range(30):
    blue.right(15)

    for side in range(8):
            blue.forward(150)
            blue.right(135)

print("Circle Spiral Shape")
