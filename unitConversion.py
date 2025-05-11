#William Van Uitert
#10/10/2023
#The purpose of this program is to show competancy in teting the abilities of a program

import math
from math import*

x_one = float(input("X Coordinate of the First Point:"))
y_one = float(input("Y Coordinate of the First Point:"))
x_two = float(input("X Coordinate of the Second Point:"))
y_two = float(input("Y Coordinate of the Second Point:"))

if((y_two-y_one) != 0 and (x_two - x_one) != 0):
    slope = str((y_two - y_one)/(x_two - x_one))
    print("The slope is: " + slope[0:4])
else:
    print("The slope is: 0")

distance = str(sqrt(pow(abs(x_two-x_one), 2) + pow(abs(y_two-y_one), 2)))

if((y_two-y_one) != 0 and (x_two - x_one) != 0):
    angle = str(atan(abs((y_two-y_one)/(x_two-x_one))) * (180/math.pi))
    polar_coordinate = "(" + distance[0:4] + " Units, " + angle[0:4] + " Degrees)"
    print("Polar Coordinate: " + polar_coordinate)
else:
    print("The distance is: 0")
    print("The angle is: 0")


