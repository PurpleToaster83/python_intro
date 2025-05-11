#William Van Uitert
#9/16/2023
#The purpose of this program is to show competancy in using if statemetns and associated operations

import numpy as np
from numpy import *


print("Let's create a matrix!")

#Find dimesnions of matrix
r = int(input("How many rows would you like?"))
c = int(input("How many columns would you like?"))

array = np.array([[0] * c] * r)
print(array)

#fill in the matrix
for row in range(0 , r):
    for column in range (0, c):
        array[row][column] = int(input("number:"))
        
print(array)

#find the determinate
def det(matrix):
        global determinate
        if(c == 2) and (r == 2):
            det_One = (matrix[0][0])*(matrix[1][1])
            det_Two = (matrix[0][1]) * (matrix[1][0])
            determinate = det_One - det_Two
            print("The determinate is: " + str(determinate))
        elif(c == 3) and (r == 3):
            linePosOne = (matrix[0][0])*(matrix[1][1])*(matrix[2][2])
            linePosTwo = (matrix[0][1])*(matrix[1][2])*(matrix[2][0])
            linePosThree = (matrix[0][2])*(matrix[1][0])*(matrix[2][1])
            det_One = linePosOne + linePosTwo + linePosThree
            line_NegOne = (matrix[2][0])*(matrix[1][1])*(matrix[0][2])
            line_NegTwo = (matrix[2][1])*(matrix[1][2])*(matrix[0][0])
            line_NegThree = (matrix[2][2])*(matrix[1][0])*(matrix[0][1])
            det_Two = line_NegOne + line_NegTwo + line_NegThree
            determinate = det_One - det_Two
            print("The determinate is: " + str(determinate))
     
        elif(c == r):
            print("I'm Sorry! I don't yet know how to do find the determinate for these dimensions.")
        else:
            print("Invalid Dimensions")

#find the inverse          
def inverse(matrice):
    if( c == 2) and (r == 2):
        det(matrice)
        opposite = np.array([[matrice[1][1], -1 * matrice[0][1]], [-1 * matrice[1][0], matrice[0][0]]])
        result = ((1/determinate) * opposite)
        print("The inverse is:")
        print(result)
    elif(c == r):
        print("I'm Sorry! I don't yet know how to do find the determinate for these dimensions.")
    else:
        print("Invalid Dimensions")

#use additon
def add(matriceA):
    print("We need to create a second matrix with the same dimensions")
    matriceB = np.array([[0]* c] * r)
    print(matriceB)

    for rowB in range(0 , r):
        for columnB in range (0, c):
            matriceB[rowB][columnB] = int(input("number:"))
            
    print(matriceB)
    addition = np.array([[0] * c] * r)
    
    for elementsAddsR in range(r):
        for elementsAddsC in range(c):
            addition[elementsAddsR][elementsAddsC] = (matriceB[elementsAddsR][elementsAddsC]) + (matriceA[elementsAddsR][elementsAddsC])

    print("The product is:")
    print(addition)

#use subtraction
def subtract(matriceA):
    print("We need to create a second matrix with the same dimensions")
    matriceB = np.array([[0]* c] * r)
    print(matriceB)

    for rowB in range(0 , r):
        for columnB in range (0, c):
            matriceB[rowB][columnB] = int(input("number:"))
            
    print(matriceB)
    subtraction = np.array([[0] * c] * r)
    
    for elementsSubR in range(r):
        for elementsSubC in range(c):
            subtraction[elementsSubR][elementsSubC] = (matriceB[elementsSubR][elementsSubC]) - (matriceA[elementsSubR][elementsSubC])

    print("The product is:")
    print(subtraction)

#use multiplication
def multiply(multiplicant):
    multiplier = float(input("What would you like to multiply the elements of the matrix by?"))
    mult = np.array([[0] * c] * r)

    for distributionR in range(r):
        for distributionC in range(c):
            mult = multiplier * multiplicant

    print("The product is:")
    print(mult)
        print(results)

#ask the user what they want to do  
operations = input("What math operation would you like to do with the matrix you created: determinate, inverse, add, subtract, multiply, or element?")
if(operations == 'determinate'):
    det(array)
elif(operations == 'element'):
    print(array)
    elementR = int(input("What row would you like to access?"))
    elementC = int(input("What column would you like to access?"))
    print(array[(elementR-1)][(elementC-1)])
elif(operations == 'inverse'):
    inverse(array)
elif(operations == 'add'):
    add(array)
elif(operations == 'subtract'):
    subtract(array)
elif(operations == 'multiply'):
    multiply(array)
else:
    print("I do not yet have the functionality to do that.")
    print("Goodbye...")
    
#TODO:add matrix multiplication
