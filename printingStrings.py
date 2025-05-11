#William Van Uitert
#8/16/2023
#This program will print multiple statments

def main():
    
    print("This program was written August 16th during the year 2023.")
    print("The author of this program is William Van Uitert.")
    print("The purpose of this program is to show competancy for print statments as well as strings.")
    
    name = input("What is your name?")
    age = input("What is your age?")
    int_age= int(age)
    year_of_birth = input("What year were you born?")
    int_year_of_birth = int(year_of_birth)
    current_year = int_age + int_year_of_birth

    
    print("Hello " + name + "!")
    print("This program is being accesed in the year " + str(current_year) + "!")
    

main()
