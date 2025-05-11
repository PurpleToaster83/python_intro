#William Van Uitert
#9/26/2023
#The purpose of this program is to show a competancy in using ASCII Code

#Be the change you wish to see in the world
message = "Be the change you wish to see in the world"

#Encoding of message
code = [0] * len(message)
binary = [0] * len(message)
for index in range(0, len(message)):
    code[index] = ord(message[index])
    binary[index] = bin(code[index])
    
display = input("Would you like to see the message in binary or ASCII (b/a):")
while not(display == "b" or display == "a"):
    display = input("Would you like to see the message in binary or ASCII (b/a):")


#print encrypted mesage
if(display == "b"):
    print(binary)
elif(display == "a"):
    print(code)
    
print("Can you guess the encoded message?")

#have the user guess the message
guess = input("Guess: ")

#compare user guess to message
if(guess == message):
    print("Correct!" + chr(0x1F389))
else:
    print("Incorrect!" + chr(0x1F4A9))
    print("The message was: " + message)



 
