# CHAPTER 10 – PRACTICE SET  

# 1. Create a class “Programmer” for storing information of few programmers 
# working at Microsoft. 

class Programmer:
    company = "Microsoft"
    def __init__(self, name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin

# p = Programmer("Shubham", 400000, 834001)
# print(p.name, p.salary, p.pin, p.company)
# r = Programmer("RShubham", 400000, 834001)
# print(r.name, r.salary, r.pin, r.company)

# 2. Write a class “Calculator” capable of finding square, cube and square root of a number. 

class Calculator:
    def __init__(self, n):
        self.n = n

    def square(self):
        print(f"The square is {self.n*self.n}")

    def cube(self):
        print(f"The square is {self.n*self.n*self.n}")

    def squareroot(self):
        print(f"The square is {self.n**1/2}")

a = Calculator(4)
# a.square()
# a.cube()
# a.squareroot()

# 3. Create a class with a class attribute a; create an object from it and set ‘a’ directly using ‘object.a = 0’. Does this change the class attribute? 

class Demo:
    a = 4

o = Demo()
# print(o.a)
o.a = 0
# print(o.a)
# print(Demo.a)


# 4. Add a static method in problem 2, to greet the user with hello. 

class Calculator:
    def __init__(self, n):
        self.n = n

    def square(self):
        print(f"The square is {self.n*self.n}")

    def cube(self):
        print(f"The square is {self.n*self.n*self.n}")

    def squareroot(self):
        print(f"The square is {self.n**1/2}")
    
    @staticmethod
    def greet():
        print("Hello World!")

a = Calculator(4)

# 5. Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats) and get fare information of train running under Indian Railways. 

from random import randint

class Train:
    def __init__(self, trainNo):
        self.trainNo = trainNo

    def book(self, frm, to):
        print(f"Ticket is booked in train no: {self.trainNo} from {frm} to {to}")

    def getStatus(self):
        print(f"Train no: {self.trainNo} is running on time")
    
    def getFare(self, frm, to):
        print(f"Ticket fare in train no: {self.trainNo} from {frm} to {to} is {randint(200, 10000)}")

t = Train(12399)
# t.book("Rampur", "Raipur")
# t.getStatus()
# t.getFare("Rampur", "Raipur")

# 6. Can you change the self-parameter inside a class to something else (say “harry”). Try changing self to “slf” or “harry” and see the effects.

class Programmer:
    company = "Microsoft"
    def __init__(shubham, name, salary, pin):
        shubham.name = name
        shubham.salary = salary
        shubham.pin = pin

p = Programmer("Shubham", 1540354, 86535)
# print(p.name, p.company, p.pin, p.salary)