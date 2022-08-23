#This is a lab where i'll be using different functions i've learned in previous lessons to:
#1. Create a machine capable of recollecting and regurgitating information
#2. Demonstrate my understanding of "print" & "input" python functions
#3. Practice how to utilize variables to create interaction between the computer and a user

name = input("Hello! May I have your name please? \n \n")
#in line 6 we took out name and set it equal to the input that we ask of the user. we use 2 new line characters to space for beautification.
print("\nHello " + name + "\n Thank you so much for coming in today!")

menu = "Black Coffees, Espressos, Lattes, Cappuccinos, Iced Mochas, & Iced Coffees \n"

print(" what do you have a taste for today? \n We're currently serving: \n \n" + menu)

order = input()

print("\nGot it mate, I'll have that ready for you in a flash. Please listen out for when we call your name with your finished " + order +"!")
print("\nHave a wonderful rest of your day, " + name)