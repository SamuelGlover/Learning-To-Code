#Here's some fundamental concepts of python
_____________________________________________________________________________________________________________________________________________________________________________

#Variables and Data Types: Python supports various data types such as integers, floating-point numbers, strings, and Boolean values. Variables are used to store data values.

#Control Structures: Python provides control structures such as if-else statements, loops, and functions to control the flow of the program.

#Functions: Functions are a set of instructions that perform a specific task. Python supports both built-in and user-defined functions.

#Object-Oriented Programming: Python supports object-oriented programming concepts such as classes, objects, inheritance, and polymorphism.

#File Handling: Python provides various functions to handle files such as reading, writing, and appending data to files.

#Exception Handling: Python provides a mechanism to handle errors and exceptions that occur during program execution.

#Modules and Packages: Python provides a modular approach to programming by allowing the creation of modules and packages that can be reused in other programs.

#Regular Expressions: Python provides support for regular expressions, which are used to search and manipulate text.

#Data Structures: Python provides various data structures such as lists, tuples, dictionaries, and sets to store and manipulate data.

#Libraries and Frameworks: Python has a vast collection of libraries and frameworks that can be used to develop complex applications quickly and efficiently.
_________________________________________________________________________________________________________________________________________________________________________________
In Python, variables are used to store data values. A variable is a name that refers to a value. The value can be of different data types such as integers, floating-point numbers, strings, lists, tuples, dictionaries, etc.

    Data types in Python are used to specify the type of data that a variable can hold. Python has several built-in data types such as int, float, str, list, tuple, dict, set, and bool. Each data type has its own set of operations and methods that can be performed on it.

    For example, if we want to store an integer value in a variable, we can declare the variable as follows:

    x = 10
    
    Here, 
    x
    is the variable name and 
    10
    is the integer value. Python automatically assigns the data type of the variable based on the value assigned to it.

Similarly, if we want to store a string value in a variable, we can declare the variable as follows:

    name = "John"
    
    Here, 
    name is the variable name and "John" is the string value. Again, Python automatically assigns the data type of the variable based on the value assigned to it.

We can also explicitly specify the data type of a variable using type casting. For example, if we want to convert a string value to an integer value, we can use the 
    int()
         function as follows:

    age = int("25")
    
    Here, age is the variable name and "25" is the string value that is converted to an integer using the 
    
    int()
         function.
    
    _________________________________________________________________________________________________________________________________________________________________________________

    In Python, an integer is a data type that represents a whole number. It is a built-in data type that is used to store numerical values without any decimal points. Integers can be positive, negative, or zero.
         
         In Python, integers are represented by the int class. We can create an integer variable by assigning a whole number to it. For example:
         
         x = 10
         y = -5
         z = 0
         In the above example, x, y, and z are integer variables that store the values 10, -5, and 0, respectively.
         
         
         Python supports all the basic arithmetic operations on integers such as addition, subtraction, multiplication, and division. For example:
         
         a = 10
         b = 5
         c = a + b   # c will be 15
         d = a - b   # d will be 5
         e = a * b   # e will be 50
         f = a / b   # f will be 2.0 (floating-point division)
         g = a // b  # g will be 2 (integer division)
         h = a % b   # h will be 0 (modulus)
         i = a ** b  # i will be 100000 (exponentiation)
    
         In the above example, 
         a and b are integer variables. The variables c, d, e, f, g, h, and i store the results of the arithmetic operations performed on a and b.
    _________________________________________________________________________________________________________________________________________________________________________________

In Python, a class is a blueprint or a template for creating objects. It is a user-defined data type that encapsulates data and functions that operate on that data.
A class defines a set of attributes and methods that are common to all objects of that class. in other words, a class is a way to define a new data type that can have its own attributes (variables) and methods (functions). 
It provides a way to organize and structure code in a modular and reusable way.

To create a class in Python, we use the 
class
 keyword followed by the name of the class. For example:
 
 class Person:
     def __init__(self, name, age):
         self.name = name
         self.age = age
 
     def say_hello(self):
         print("Hello, my name is", self.name, "and I am", self.age, "years old.")

        In the above example, we have defined a class called 
        Person.

         The class has two attributes (name and age) and one method (say_hello). The __init__ method is a special method that is called when an object of the class is created. 
        It initializes the attributes of the object with the values passed as arguments. 
        
        To create an object of the Person class, we can use the following code:
        
        person1 = Person("John", 25)
        In the above code, we have created an object of the 
        Person
         class called person1. We have passed the values "John" and 25 as arguments to the init method, which initializes the name and age attributes of the object.
        
        
        We can call the say hello method on the person1 object as follows:
        
        person1.say_hello()
        This will output the following message:
        
        Hello, my name is John and I am 25 years old.

        _________________________________________________________________________________________________________________________________________________________________________________
