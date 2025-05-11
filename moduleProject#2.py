#William Van Uitert
#09/03/2023
#The purpose of this program is to show competancy in math operations by calculating stock growth

#get stock information
name = input("Fund or stock name:")
numShares = int(input("Number of stocks:"))
current_price = float(input("Current share price:"))
original_price = float(input("Price of share at purchase:"))
time = float(input("Number of years since purchase:"))

if(time < 1):
    days = time * 365
    unit = 'days!'
else:
    days = time
    unit = 'years!'
    
#calculations
moneyMade = numShares * (current_price - original_price)
growth = (current_price / original_price) - 1
percent = (growth / time) * 100
disPercent = str(abs(percent))[0:5]

#response to stock information
if(moneyMade > 0):
    print("You have made $" + str(moneyMade) + " in " + str(days) + " " + unit)
    print(name + " grew about " + disPercent + "% per year")
elif(moneyMade < 0):
    print("You have lost $" + str(abs(moneyMade)) + " in " + str(days) + " " + unit)
    print(name + " depreciated about " + disPercent + "% per year")
else:
    print(name + " didn't change and you have the same amount of money")


