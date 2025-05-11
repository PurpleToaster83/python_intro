#William Van Uitert
#9/6/2023
#The purpose of this program is to show competancy in creating and using a personal made function

import turtle

face = turtle.Turtle()
eyes = turtle.Turtle()
mouth = turtle.Turtle()

face.speed(12)
eyes.speed(10)
mouth.speed(10)

xpos = int(input("X Position:"))
ypos = int(input("Y Position:"))
radius = int(input("Face Size:"))

xpos_sec = int(input("Second X Position:"))
ypos_sec= int(input("Second Y Position:"))
radius_sec = int(input("Second Face Size:"))

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


smileyFace(xpos, ypos, radius)
smileyFace(xpos_sec, ypos_sec, radius_sec)

