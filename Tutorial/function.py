# A function is a group of statements performing a specific task. 
# When a program gets bigger in size and its complexity grows, it gets difficult for a 
# program to keep track on which piece of code is doing what! 
# A function can be reused by the programmer in a given program any number of 

# function definition
def func1(): 
    print('hello')

func1() # This is called function call.

def greet():
    print("Good day")

greet()

# There are two types of functions in python: 
# Built in functions (Already present in python) 
# User defined functions (Defined by the user) 
# Examples of built in functions includes len(), print(), range() etc. 
# The func1() function we defined is an example of user defined function.

# FUNCTIONS WITH  ARGUMENTS

# A function can accept some value it can work with. We can put these values in the parentheses. 
# A function can also return value as shown below: 

def greet(name): 
    gr = "hello"+ name  
    return gr  
                    
a = greet ("shubham") 
# a will now contain "hello shubham"  

# DEFAULT PARAMETER VALUE  
# We can have a value as default as default argument in a function. 
# If we specify name = “stranger” in the line containing def, this value is used when no argument is passed. 

def who(name="stranger"): # function body
    print(name) 

who() # name will be "stranger" in function body (default) 
who("shubham") # name will be "harry" in function body (passed)