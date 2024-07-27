# Inheritance is a way of creating a new class from an existing class. 

# Syntax: 

# class Employee:  # Base class  
    # Code 
 
# class Programmer(Employee): # Derived or child class 
    # Code 


# Simple Class
# class Employee:
#     company = "ITC"
#     name = "Shubham"
#     def greet(self):
#         print(f"Hello {self.name}")

# class Programmer:
#     company = "ITC Infotech"
#     def greet(self):
#         print(f"Hello {self.name}")
#     def showcompany(self):
#         print(f"{self.name} work's in {self.company}")

# a = Employee()
# b = Programmer()

# print(a.company, b.company)


# Inheritance
class Employee:
    company = "ITC"
    name = "Shubham"
    def greet(self):
        print(f"Hello {self.name}")

class Programmer(Employee):
    company = "ITC Infotech"
    def showcompany(self):
        print(f"{self.name} work's in {self.company}")

a = Employee()
b = Programmer()

print(a.company, b.company)

# We can use the method and attributes of ‘Employee’ in ‘Programmer’ object. 
# Also, we can overwrite or add new attributes and methods in ‘Programmer’ class. 

# TYPES OF INHERITANCE  
# • Single inheritance 
# • Multiple inheritance 
# • Multilevel inheritance 


# SINGLE  INHERITANCE  
# Single inheritance occurs when child class inherits only a single parent class.  

# syntax

class Employee:
    company = "ITC"
    name = "Shubham"
    def greet(self):
        print(f"Hello {self.name}")

class Programmer(Employee):
    company = "ITC Infotech"
    def showcompany(self):
        print(f"{self.name} work's in {self.company}")

a = Employee()
b = Programmer()

print(a.company, b.company)

# MULTIPLE INHERITANCE  
# Multiple Inheritance occurs when the child class inherits from more than one parent classes.
 
#  syntax

class Employee:
    company = "ITC"
    name = "Shubham"
    def greet(self):
        print(f"Hello {self.name}")

class Coder:
    language = "Python"
    def printLanguage(self):
        print(f"Out of all the language here is your language: {self.language}")

class Programmer(Employee, Coder):
    company = "ITC Infotech"
    def showcompany(self):
        print(f"{self.name} work's in {self.company}")

a = Employee()
b = Programmer()

b.greet()
b.showcompany()
b.printLanguage()
 
# MULTILEVEL  INHERITANCE  
# When a child class becomes a parent for another child class.                                                        

# syntax

class Employee:
    a = 1

class Programmer(Employee):
    b = 2

class Manager(Programmer):
    c = 4

o = Employee()
print(o.a)
 
 
 
 
 
