#William Van Uitert
#9/15/2023
#The purpose of this program is to show competancy using arrays, loops, and comparison logic

subjects = ['Computer Science', 'Math', 'Science', 'Social Studies', 'English']

favorite = input("What is your favorite subject in school?")

for iteration in range(len(favorite)):
    if(favorite == subjects[(iteration - 1)]):
        print("That was in position " + str(iteration) + " in my lists of favorite subjects too!")
if(favorite != subjects[0]) and (favorite != subjects[1]) and (favorite != subjects[2]) and (favorite != subjects[3]) and (favorite != subjects[4]):
        print("We don't have any favorite subjects in common")

print("My favorite subjects are:")
for list in range(6):
    print(list, subjects[(list -1)])

