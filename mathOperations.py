#William Van Uitert
#9/2/2023
#The purpose of this program is to show competancy in using math operations in Python

from math import*
import math

def main():
    print("Think about a shape and its dimesnsions and answer the following prompts accordingly (no units needed). The computer will try to guess the shape you are thinking about and output its volume and surface area.")
    print("The possible shapes are: cube, sphere, cylinder, cone, square pyrimid, and rectangular prism")
    print("Answer N/A to prompts about dimensions that aren't applicable to your shape")

    h = input("Height:")
    l = input("Length:")
    w =input("Width:")
    r = input("Radius:")

    if(h == "N/A" or h == "n/a") and (l == "N/A" or l == "n/a") and (w == "N/A" or w == "n/a"):
        print("Your shape is a sphere!")
        v = (4/3) * (math.pi) * pow(int(r), 3)
        surface_area = 4 * (math.pi) * pow(int(r), 2)
        print("Volume = " + str(v))
        print("Surface Area = " + str(surface_area))
        
    elif(h != "N/A" or h != "n/a") and (l == "N/A" or l == "n/a") and (w == "N/A" or w == "n/a"):
        slantHeight = input("Does your shape have a slant height?")
        
        while not(slantHeight == "yes") or (slantHeight == "no"):
            slantHeight = input("Please enter yes or no:")
            
        if(slantHeight == "Yes" or slantHeight == "yes"):
            print("Your shape is a cone!")
            v = (1/3) * (math.pi) * int(h) * pow(int(r), 2)
            surface_area = (math.pi * int(r)) * (int(r) + sqrt(pow(int(h), 2) + pow(int(r), 2)))
            print("Volume = " + str(v))
            print("Surface Area = " + str(surface_area))

        elif(slantHeight == "No" or slantHeight == "no"):
            print("Your shape is a cylinder!")
            v = math.pi * int(h) * pow(int(r), 2)
            surface_area = (2 * math.pi * pow(int(r), 2)) + (2 * math.pi * int(r) * h)
            print("Volume = " + str(v))
            print("Surface Area = " + str(surface_area))
            
    elif(int(h) == int(w)) and (int(w) == int(l)) and (r == "N/A" or r == "n/a"):
        slantHeight = input("Does your shape have a slant height?")

        while not(slantHeight == "yes" or slantHeight == "Yes" or slantHeight == "no" or slantHeight == "No"):
            slantHeight = input("Please enter yes or no:")

        if(slantHeight == "Yes" or slantHeight == "yes"):
            print("Your shape is a square pyrimid!")
            v = (int(l) * int(w) * int(h))/3
            base_diagnol = sqrt(2) * int(l)
            slant_height = sqrt(pow((base_diagnol/2), 2) + pow(int(h), 2))
            surface_area = pow(int(l), 2) + (2 * int(l) * slant_height)
            print("Volume = " + str(v))
            print("Surface Area = " + str(surface_area))

        elif(slantHeight == "No" or slantHeight == "no"):
            print("Your shape is a cube!")
            v = pow(int(l), 3)
            surface_area = 6* pow(int(l), 2)
            print("Volume = " + str(v))
            print("Surface Area = " + str(surface_area))
            
    elif(h != "N/A" or h != "n/a") and (l != "N/A" or l != "n/a") and (w != "N/A" or w != "n/a") and (int(h) != int(w)) or (int(w) != int(l)) or(int(l) != int(h)) and (r == "n/a" or r == "N/A"):
        print("Your shape is a rectangular prism!")

        v = int(l) * int(h) * int(w)
        surface_area = (2 * int(l) * int(w)) + (2 * int(w) * int(h)) + (2 * int(h) * int(l))
        print("Volume = " + str(v))
        print("Surface Area = " + str(surface_area))

    else:
        print("I am unable to calculate information and guess your shape with my knowledge.")

main()
