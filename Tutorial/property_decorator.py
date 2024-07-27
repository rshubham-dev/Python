# @PROPERTY DECORATORS  
# Consider the following class: 
# class Employee: 
#     @property 
#     def name(self): 
#         return self.ename 
# If e = Employee() is an object of class employee, we can print (e.name) to print the 
# ename by internally calling name() function. 

class Employee:
    a = 1
    @classmethod
    def show(cls):
        print(f"The class attribute of a is {cls.a}")
    
    @property
    def name(self):
        return f"{self.fname} {self.lname}"
    
    @name.setter
    def name (self, value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]

e = Employee()
e.a = 44

e.name = "Shubham Kumar"
print(e.fname)

e.show()