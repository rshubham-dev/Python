# Solving a problem by creating object is one of the most popular approaches in programming. This is called object-oriented programming. 
# This concept focuses on using reusable code (DRY Principle).  
 
# A class is a blueprint for creating object.

# Syntax
# class Employee: # Class name is written in pascal case 
    # Methods & Variables

# An object is an instantiation of a class. When class is defined, a template (info) is defined. Memory is allocated only after object instantiation. Objects of a given class can invoke the methods available to it without revealing the implementation details to the user. – Abstractions & Encapsulation! 

class Employee:
    language = "Python"  # this is a class attribute 
    salary = 17000

# An attribute that belongs to the class rather than a particular object.

shubham = Employee()
print(type(shubham))

print(shubham.language)
print(shubham.salary)

shubham.name = "Shubham" # this is a instance attribute
print(shubham.name)

# An attribute that belongs to the Instance (object). Instance attributes, take preference over class attributes during assignment & retrieval. 

shubham.language = "Javascript"
print(shubham.language)


