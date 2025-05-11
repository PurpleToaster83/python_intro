import random
#William Van Uitert
#8/17/2023
#The purpose of this program is to show competancy coding user input  and indexing characters

run = True

if(run == True):
    #introduction to state purpose of code
    name = input("What is your name?")
    print("Hello " + name)
    print("My name is ZIP and I am a chatbot.")

    #asks user a question
    animal = input("Can you name an animal that starts with 'D'?")
    while not(animal[0] == 'd') or (animal[0] == 'D'): #ask the question again until answer starts with a 'D'
        animal = input("That animal starts with a '" + animal[0] + "'. Please enter an animal that starts with the letter 'D':")
    #responds to user input
    if(animal == 'dolphin') or (animal == 'Dolphin'):
        print("Dolphins are fascinating creatures.")
    elif(animal == 'deer') or (animal == 'Deer'):
        print("Correct")
    elif(animal == 'donkey') or (animal == 'Donkey'):
        print("Yes")
    elif(animal == 'dog') or (animal == 'Dog'):
        print("In my opinion cats are better.")
    elif(animal == 'dove') or (animal == 'Dove'):
        print("Very good")
    elif(animal[0] == 'd') or (animal[0] == 'D'):
        print("I am not familiar with that animal but it does start with a 'D'.")

    #asks user if they want to countinue
    countinue = input("Enter 'Exit' at any time if you would like to close the chatbot. Enter enything else if you would like to be asked another question.")
    if(countinue == 'exit') or (countinue == 'Exit'): #program goes to exit code
        run = False
    else: #program countinues
        countinue = True

    while(countinue == True): #will countinuously ask until countinue is false
        randNum = random.randint(1, 2) #creates coin
        coin = input("Heads or Tails?")
        #compares user input to coin results
        if(coin == 'Heads') or (coin == 'heads') and (randNum == 1):
            print("The coin was Heads. You Win!")
        elif(coin == 'Tails') or (coin == 'tails') and (randNum == 2):
            print("The coin was Tails. You Win!")
        elif(coin == 'exit') or (coin == 'Exit'):
            countinue = False
            run = False
        elif(coin != 'Heads') and (coin != 'heads') and (coin != 'Tails') and (coin != 'tails'):
            print("Please enter heads or tails")
        else:
            print("You Lose!")
            
#Code exits
if(run == False):
    print("Goodbye " + name + "...")
