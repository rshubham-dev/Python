# Self Parameter
# Self refers to the instance of the class. It is automatically passed with a function call from an object. 

class Employee:
    language = "Python"  
    salary = 17000

    def getInfo(self):
        print(f"The language is {self.language}. the salary is {self.salary}")
    
    @staticmethod   # decorator to mark greet as a static method  
    def greet(): 
        print("Hello user") 

shubham = Employee()
shubham.getInfo()

# STATIC METHOD 
# Sometimes we need a function that does not use the self-parameter.