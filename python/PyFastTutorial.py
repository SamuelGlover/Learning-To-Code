#Notes on Python as fast as possible by tech with tim on youtube
#Link: https://youtu.be/VchuKL44s6E

#Python is used for: general purpose
#python is very easy to learn, versatile, and easy to write
#Core advantage(s): simple, ez syntax, fast dev

______________________________________________________________
#Core Data Types:

#Int- Any whole number with no decimal
#Float- Any number with a decimal
#String- Any quoted text of a sequence of characters
#-Single vs double quotes doesn't matter, just be consistent
#to embed quotes use opposite quote type to wrap
#Bool or Boolean- one of two values. true or false, 1 or 0

#These are your 4 core data types

_______________________________________________________________
#Output & Printing

print("Hello World")
#print is the simple function to output to a console on run
#Hello World is the string
#you can only print data types.
#You can pass arguments into Print functions

print("Hello", "end", 87, False, end="\n" )
print("Hello")

#"\n" moves you to the next line

#Lets talk variables
#In python they're easy to create:
#variable name + space + equal sign + some value.
#Variables store information for recall at a later time.

hello = "sam"
world = "world"

print(hello, world)
print(world, hello)
#Variable naming conventions:
#1) no special characters except underscore
#2) cannot start with a number
#3) in python underscores typically denote separation
#4) this separation is known as snakecase, words being put together is called camelcase
________________________________________________________________________

#Lets talk retrieving user inputs
#its simple too.

input("prompt here")

#inputs need prompts
#Unlike in print statements an input must contain a string

input("Name: ")

#now to store this value
#to do so we need to assign this input to a variable.

Name = input("Name: ")
print(Name)

#of course you can collect multiple variables at once.

Name = input("Name: ")
Age = input("Age: ")
print("Hello ", name, "you are", age, "years old.")

#say age is 21 and name is Sam. The python machine would read back:
#"Hello Sam you are 21 years old."

#thats it for input]
_____________________________________________________________________

#Arithmetic Operators!!

#+,-,*,/,**,//,%,
#Addition, subtraction, multiplication, division, exponent, 
#floor division (Gives int result), and Mod (Returns remainder after division) respectively


#When preforming these, we have to make sure the Data types on either sides of the operands are:
#1)the same data types 
# or 
#2) both numbers.

#you will get an error if data types are not the same.abs(

x = 9
y = 3
result = x/y
print(result)

#The division operator always returns a float. use the int function to convert:

x = 9
y = 3
result = int(x / y)
print(result)

#Lets talk order of operations in python

#Brackets
#Exponents 
#Division
#Multiplication
#Addition
#Subtraction

#Int & Mod fall lowest on the order of operations below addition and subtraction

#Lets do an example

num = input("Number: ")
print(num - 5)

#This will cause an error saying it doesn't know what to do with a string here.
#Why is this?

#Well, that's because anything you type in response to an input will come in as a string,
#So even though num looks like an int to us, it's set equal to a string, making it a string too.
#We have to convert it so it follows the rules our machine understands.

#To do that we can use an int function

num = input("Number: ")
print(int(num) - 5)

#This tells the computer to take the input we give and convert it to an int, then subtract 5
#You can do this with other functions too such as the float function

num = input("Number: ")
print(float(num) - 5)

#Remember, float always returns float to retain the level of original precision
__________________________________________________________________________________________________

#String Methods!!!!

#First we have to define a method
#lets start by creating a variable

hello = "hello"

#we've set the variable hello equal to the string "Hello"
#Let's talk about the type function

hello = "hello"
print(type(hello))

#This will return the data type of a variable. in this case it's an instance of the class string.
#We'll touch more on this later.

#So what does this have to do with methods?
#A method is something with a .operator

hello = "hello".upper()
print(hello)

#What do you think will happen here???
#upper is the method, and it will uppercase the entire string
#you also don't have to call it like that, it can be done as:

hello = "hello"
print(hello.upper)

#and it will do the same thing.

#There is
#.upper-uppercase string
#.lower-lowercase string
#.capitalize-Uppercases first letter and sentence formats
#.count-counts within string (sensitive to case)
#There are more of these, but these are basic string methods. They chain btw.

hello = "hello World".upper()
print(hello.lower().count("o"))

__________________________________________________________________________________________________


#String Multiplication & Addition!

#you can multiply a string by an integer to repeat something a certain amount of times
#you can add two strings together (this is called concatenation )

_____________________________________________________________________________________

#CONDITIONS/ CONDITIONAL OPERATORS!!!

#A condition is something that evaluates or compares two variables/ data types and delivers a true or false value based on comparison

#Exe: Is X equal to Y? Yes or No, True or false.(Boolean)

# == -checks for equality
# != -checks for inequality
# <= -less than or equal to
# >= -greater than or equal to
# <  -less than
# >  -greater than

#these are the core conditional operators, there are more, but this is enough to cover for now

#Interesting about strings:
#you can compare strings using < & >

print("a" > "Z")

#This will print true, but why??

#The reason is because every character in python is represented by an asci code
#You can see these by looking for a character's ordinal value.

print(ord("a"))

#the ordinal value of a is 97

print(ord("Z"))

#the ordinal value of Z is only 90, so python will tell you lowercase a is greater than uppercase Z

#if you tried this with b it would be false as b has an ordinal value of 98

#Results compare left to right, and you can store them in variables as well

#CHAINED CONDITIONALS

#multiple conditions combined to create a larger condition

X = 7
y = 8
z = 0

result1 = x == y
result2 = y > x
result3 = z - 2 < (x + 2)

#conditional operators have lower precedence than all arithmetic operators.'
#look at result 3, this will not go left to right. it'll combine on the left, then the right, 
# then carry out the function of the conditional operator.

#we can use a few key words to chain conditionals together:

#1)and
#2)or
#3)not

#like this:

result4 = result1 or result2 
print(result4)

#This will look at the left and right and say if one is true, the entire condition is true. 
#Both sides must be false for "or" to return a false statement

result4 = result1 or result2 
print(not(result4))

#not will make something the opposite. true becomes false and false becomes true
#it can also be done as:

result4 = result1 or not result2 
print(result4)

#This will take whats on the right of "not" and flip it

print(not true)

#prints false.

#now lets talk about and

result4 = result1 and result2 
print(result4)

#if both sides are true it'll return true,
#otherwise it is false.

#and & or can be combined.

result4 = result1 and result3 or result2 
print(not(result4))

#There is an order of operations for and, or, not though:

#1)not
#2)and
#3)or

#keep this in mind because its important for how you write expressions.

____________________________________________________________________________________________________

#IF/ELSE?ELIF statements!!!

#here's the fun shit!