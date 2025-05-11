#William Van Uitert
#10/12/2023
#The prupose of this program is to demonstrate copetancy in the skills discuessed throughout the course

import random
    
def rockPaperScissors():
    userChoice = input("Rock, Paper, or Scissors (R/P/S)")
    userChoice = userChoice.capitalize()
    
    if(userChoice == "R"):
        print("You Chose: Rock")
        choiceValue = 0
    elif(userChoice == "P"):
        print("You Chose: Paper")
        choiceValue = 1
    elif(userChoice == "S"):
        print("You Chose: Scissors")
        choiceValue = 2
    else:
        print("You didn't answer. You Lose!")


    options = [0, 1, 2]
    computerChoice = random.choice(options)

    if(computerChoice == 0):
        computer_object = "Rock"
    elif(computerChoice == 1):
        computer_object = "Paper"
    elif(computerChoice == 2):
        computer_object = "Scissors"

    print("The Computer Chose: " + computer_object)
    if(userChoice == "R" or userChoice == "P" or userChoice == "S"):
        if(choiceValue == computerChoice):
            print("Draw!")
        elif((choiceValue + 1) % 3 == computerChoice):
            print("You Lose!")
        else:
            print("You Win!")
    print("")
    
while(0==0):
    rockPaperScissors()
  
