# __INIT__() CONSTRUCTOR 
# __init__() is a special method which is first run as soon as the object is created. 
# __init__() method is also known as constructor. 
# It takes ‘self’ argument and can also take further arguments.

class Employee:
    # language = "Python"  
    # salary = 17000

    def __init__(self, name, salary, language): # dunder method which is automatically called
        self.name = name
        self.salary = salary
        self.language = language
        print("I am creating an object")

    def getInfo(self):
        print(f"The language is {self.language}. the salary is {self.salary}")
    
    @staticmethod   # decorator to mark greet as a static method  
    def greet(): 
        print("Hello user") 

shubham = Employee("Shubham", 17000, "Javascript")
print(shubham.name, shubham.language, shubham.salary)  