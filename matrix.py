from numpy import *

r = int(input("How many rows would you like?"))
c = int(input("How many columns would you like?"))

array = array([[0] * c] * r)
print(array)

for row in range(0 , r):
    for column in range (0, c):
        array[row][column] = int(input("number:"))

print(array)
elementR = int(input("What row would you like to access?"))
elementC = int(input("What column would you like to access?"))
print(array[(elementR-1)][(elementC-1)])
    
    
