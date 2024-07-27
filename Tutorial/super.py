# SUPER() METHOD   
# super() method is used to access the methods of a super class in the derived class. 

# super().__init__() 
# # __init__() Calls constructor of the base class 



class Employee:
    def __init__(self):
        print("Constructor of Employee")
    a = 1

class Programmer(Employee):
    def __init__(self):
        print("Constructor of Programmer")
    b = 2

class Manager(Programmer):
    def __init__(self):
        super().__init__()
        print("Constructor of Manager")
    c = 4

# e = Employee()
# print(e.a)
# p = Programmer()
# print(p.a)
m = Manager()
print(m.a, m.b, m.c)