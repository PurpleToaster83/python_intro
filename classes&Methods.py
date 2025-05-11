#William Van Uitert
#9/30/2023
#The purpose of this program is to show competancy in creating and using objects as classes

import random


class Superhero:
    
    def __init__(self, name = "", true_name = "", power_one = "", power_two = "", power_three = "", strengthPts = 0):
        self.name = name
        self.true_name = true_name
        self.power_one = power_one
        self.power_two = power_two
        self.power_three = power_three
        self.strengthPts = strengthPts

    def addStrengthPts(self, points):
        self.strengthPts = self.strengthPts + points
        
    def originStory(self, place = "", causeOfPowers = "", resultsOfCause = "", nemesis = ""):
        self.place = place
        self.causeOfPowers = causeOfPowers
        self.resultsOfCause = resultsOfCause
        self.nemesis = nemesis
        story = "One day " + self.true_name + " was doing his normal activities when all of a sudden a " + self.causeOfPowers + " interupts him! As a result he " + self.resultsOfCause + " giving him the ability to " + self.power_one + ", becoming " + self.name + "." + " Now, " + self.name + " saves the digital world by fighting his arch-enemy " + self.nemesis + "."
        print(story)

    def transform(self, normal_points):
        self.normal_points = normal_points
        print(self.true_name + " transfroms into " + self.name)
        self.strengthPts = self.normal_points + self.strengthPts
        print(self.true_name + "'s strenght goes from " + str(self.normal_points) + " to " + str(self.strengthPts))

        
        
        
print("Let me tell you the about an awesome super hero!")

newSuperhero = Superhero("Byte Bender", 'Benjamin ChipROM', "access any code and manipulate it to his will", "project coded messages directly into the minds of others", "see and interpret data streams relating to vunerabilities in the real wolrd", 50)
print(newSuperhero.true_name + "!")
print("His alter ego is " + newSuperhero.name)
newSuperhero.originStory("work", "lightning strike", "merged with the digital world", "the Undivisible Zero and his side-kick Binary Boy")
newSuperhero.transform(20)

alive = True

enemies_defeated = 0
if(alive == True):
    while(alive == True):
        if(enemies_defeated >= 1):
            strengthE_limit = 20*(1.5* enemies_defeated)
        else:
            strengthE_limit = 100
        strengthE_min = (10 * enemies_defeated) + 1
        enemy_strength = random.randint(strengthE_min, strengthE_limit)
        
        print("The enemy is " + str(enemy_strength) + " strong")
        print("You are " + str(newSuperhero.strengthPts) + " strong")
        fight = input("Would you like to challenge them? (y/n/#)")
        if(fight == "y" and newSuperhero.strengthPts > enemy_strength and enemies_defeated <= 9):
            print("You Won!")
            enemies_defeated = enemies_defeated + 1
            if(enemies_defeated >= 1):
                newSuperhero.addStrengthPts(10)
                        
        elif(fight == "y" and newSuperhero.strengthPts <= enemy_strength and enemies_defeated <= 9):
            print("You Lost")
            alive = False
        elif(fight == "n" and enemies_defeated <= 9):
            print("You ran away")
        elif(fight == "#" and enemies_defeated <= 9):
            print(enemies_defeated)
        elif(enemies_defeated == 10):
            print(newSuperhero.name + " encountered " + newSuperhero.nemesis)
            c_choice = [0, 1, 2]
            computer = random.shuffle(c_choice)
            choice = input("rock, paper, or scissors:")
            if(choice == "rock"):
                answer = 0
            elif(choice == "paper"):
                answer = 1
            else:
                answer = 2

            if(answer == computer):
                print("It's a Draw. Battle again another time")
            elif( (answer + 1) % 3 == computer):
                print("You Lost to " + newSuperhero.nemesis)
            else:
                print("You defeated " + newSuperhero.nemesis + " and saved the world")
            
            alive = False
        else:
            print("You took to long to answer correctly and was killed")
            alive = False
else:
    print("The End")
