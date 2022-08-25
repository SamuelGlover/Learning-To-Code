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

#IF/ELSE/ELIF statements!!!

#here's the fun shit!

#Let's start with if and else
if condition:
    Print("...")
    Print("...")
else:
    Print("ew.")

#if something, then do this basically, if it's anything else, do this.
#else can only come after if.
#pretty self explanatory.

#what if you need to check multiple things though?

#time for ELIF statements.abs(

x = input("Name: ")

if x == "Sam":
    Print("Hi Sam!")
    Print("I think ur awesome!")
elif x == "Jim":
    Print("Sup Jim")
else:
    Print("ew.")

#you can only have one if & one else, but as many elif statments as you need.
#elif must come after if and before else.
#you don't have to have an else statement to have an elif btw
#you can nest ifs inside of ifs and such however indentation becomes paramount,
#since that helps our python machine determine what to print if the statement is true

____________________________________________________________________________________________________

#Let's talk Collections.

#What is a collection?
#A: an ordered or unordered group of elements.

#Let's talk two types of collections real quick:
#1)Lists
#2)Tuples

#LISTS!!!

#Lists are denoted by square brackets with elements within
#Elements are simply some form of data type

x = [4, true, "hi"]

#please note that unlike many other languages, the elements don't have to be the same data type in these lists
#We put integers, strings, and values.

#Lists store bunches of elements in an ordered collection.
#The order in which we enter things actually matters and is maintained in lists.

#How do we access lists, how do we deal with lists, and what do we do with them?
 
 #you can define a list by opening square brackets and defining an element.
 #an empty list can be created by leaving the square brackets empty.

 #to access a list you can use functions. lets start with Len

 #len will tell us the length of the list, however it also works on strings and a couple other things.

x = [4, true, "hi"]
y = "hi"
print(len(x))

#and it would tell you the list had a length of 3

#You also can append to lists, let's look at this

x = [4, true, "hi"]
y = "hi"
x.append("hello")
print(len(x))

#This adds the string "hello" to the end of the list
#if you printed x here you would get "4, true, hi, hello" in order.

#extend is next

x = [4, true, "hi"]
y = "hi"
x.append("hello")
x.extend([4,5,6,7,8,9])
print(len(x))

#extend would look through the list you inputted and append each piece of the list to the end of your existing list

#how would you remove something?
#By popping it off obviously!
#pop removes and returns the last element of a list

x = [4, true, "hi"]
y = "hi"
x.append("hello")
x.extend([4,5,6,7,8,9])
print(len(x))
print(x.pop)

#another argument of pop the index of the element we want to remove.
#every number in a list is numbered with a number called it's index.
#the first position in an list is zero


x = [4, true, "hi"]
y = "hi"
x.append("hello")
x.extend([4,5,6,7,8,9])
print(len(x))
print(x.pop(0))

#this would remove the first element from the list, in this case, the integer 4

#what if we just want to access our list?
# We can access our list like this:

x = [4, true, "hi"]
y = "hi"
x.append("hello")
x.extend([4,5,6,7,8,9])
print(len(x))
print(x[1])

#instead of popping a value off, we now print the index within the square brackets,
#in this case, it's the value "true"

#we can also change values:

x = [4, true, "hi"]
y = "hi"
x[1] = False
x.append("hello")
x.extend([4,5,6,7,8,9])
print(len(x))
print(x[1])

#now when we print, we'll end up seeing that instead of the value "true", 
#the list has been changed and that the value there is now "False"

#why can we do this?

#lists are mutable: that means x doesn't store a copy to the list, 
#but instead a reference to a list

#this means all elements can be changed.

#to make a copy of the list you'd need 

y = x[:]

#the x[:] is important here, we'll talk about how that works in a bit,
#but right now whats important is that because you made a copy, the change won't apply to the other list.


#TUPLE TIME!

#tuples work the same as lists;
#except they use round brackets "()", and are immutable.
#You can't append, change or remove elements of tuples.
#once it's been defined, to make changes we have to redefine it.
#You will get errors if you try to treat it as mutable.

____________________________________________________________________________________________________

#FOR LOOPS!!

#For loops allow you iterate a set amount of times.
#a While loop however runs an indefined number of times based on a condition.

#we know how many times a for loop will run relatively.

#Let's focus on the for loop real quick

#Here's a basic for loop:

for i in range(10)
print(i)

#There's a lot of stuff happening here right??? let's talk about it.

#This would print 0-9, 10 numbers
#i is considered a "counter variable" or an "iterator"
#range is a function that creates a collection of numbers based on the inputs we give it.

# so for some variable, in some range, we print a certain thing

#let's talk inputs we can give to range.

start, stop, step

#we're allowed to put up to three arguments inside a range function.

#Where do we start, where do we step, then where do we stop?

#if there's only one argument by default it will be a stop argument. 
#You will start at 0 and go to the number in range, but not include that number.
#two arguments is start and stop:

for i in range(1,10)
print(i)

#this would print numbers 1-9

#3 is start stop & step, and step denotes increments every time.
#step defaults to one but can be incremented by a negative number

for i in range(10,-1, -2)
print(i)

#this would print numbers in descending order from 10, so 10, 8, 6, 4, 2, 0

#making sense yet?

#lets loop through a list next

for i in [3,4,5,6,7,88]
print(i)

#this will step through everything in this list.

#Now let's try keeping track of an index instead

x = [3,4,42,3,2,4]

for i in range(len(x))
print(x[i])

#This will go up to but not include the last index of x, that means this will print 6.
#We can make life simpler and. do this another way

x = [3,4,42,3,2,4]

for i in enumerate(x)
    print(i, element)

#enumerate will create indexes and values for all the elements in our list.
#we print all the indexes with i, and then all the elements with element.

________________________________________________________________________________________________

#WHILE LOOPS:

x = [3,4,42,3,2,4]

i = 0
while i <10 
    print("run")
    i += 1
    i *= 2

#lets talk break statements


i = 0
while true: 
    print("run")
    i += 1
    if i == 10:
        break
 ________________________________________________________________________________________________

#SLICE OPERATOR

print(sliced)

#take a slice of a collection and do something with it.

sliced = [start:stop:step]

print (sliced)

#start at an index, go to a index but don't include it, then step by a value.
#if we only include a colon and a number, it's saying stop at that index
#empty brackets denote a beginning or an end

sliced = x[::-1]
print(sliced)

#this reverses a list quickly. says start at the beginning, stop at the end, and step by -1

#this covers the basics of slice operators, they work on tuples.

________________________________________________________________________________________________

#Sets

#sets are an unordered, but unique collection of elements.
#there can be no element duplicates in a set
#order/frequency isn't kept track of
#seeing if something is there or now.
#sets can be done fast.

#lookups, removals, and additions.
#in lists, this is probably the fastest way to remove an element.

#we can remove the first element from a list, you need to shift all the other positions
#but with sets you don't have to preform a bunch of other operations.
#used for situations where you don't care about frequency or order.

#written like this:

x = set()
s = {4, 32, 2, 2}

#sets are actually denoted by {} but using them for empty sets will create a dictionary which you don't want right now.
#instead make sure you use set()

#remember, set tracks presence, not order or frequency.

s.add() #adds to a set
s.remove() #removes from set

print(4 in s) #checks for something in a set and gives a boolean (true or false)

#this happens in constant time which is incredibly fast

#multiple sets can be done as s and s2 and s3 and so on...

#a few other operations can be done in sets

print(s.union)
print(s.intersection)

and so on