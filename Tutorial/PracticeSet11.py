# CHAPTER 11 - PRACTICE SET  
# 1. Create a class (2-D vector) and use it to create another class representing a 3-D vector. 

class TwoDVector:
    def __init__(self, i, j):
        self.i = i
        self.j = j
    def show(self):
        print(f"The vector is {self.i}i + {self.j}j")

class ThreeDVector(TwoDVector):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.k = k
    def show(self):
        print(f"The vector is {self.i}i + {self.j}j + {self.k}k")

a = TwoDVector(2, 4)
# a.show()
b = ThreeDVector(6, 8, 10)
# b.show()

# 2. Create a class ‘Pets’ from a class ‘Animals’ and further create a class ‘Dog’ from ‘Pets’. Add a method ‘bark’ to class ‘Dog’. 

class Animals:
    pass

class Pets(Animals):
    pass

class Dog(Pets):
    @staticmethod
    def bark():
        print("Bow Bow Bow!")

d = Dog()
# d.bark()

# 3. Create a class ‘Employee’ and add salary and increment properties to it. 
# Write a method ‘salaryAfterIncrement’ method with a @property decorator with a setter which changes the value of increment based on the salary. 

class Employee:
    salary = 17000
    increment = 20

    @property
    def salaryAfterIncrement(self):
        return (self.salary + self.salary * (self.increment/100))

    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, salary):
        self.increment = ((salary/self.salary)-1)*100

e = Employee()
e.salaryAfterIncrement =  20400
# print(e.increment)


# 4. Write a class ‘Complex’ to represent complex numbers, along with overloaded operators ‘+’ and ‘*’ which adds and multiplies them.

class Complex:
    def __init__(self, r, i):
        self.i = i
        self.r = r

    def __add__(self, c2):
        return Complex(self.r + c2.r, self.i + c2.i)
    
    def __mul__(self, c2):
        return Complex(self.r + c2.r, self.i + c2.i)
    
    def __str__(self):
        return f"{self.r} + {self.i}"

c1 = Complex(1, 2)
c2 = Complex(4, 5)
# print(c1+c2)

# 5. Write a class vector representing a vector of n dimensions. Overload the + and * operator which calculates the sum and the dot(.) product of them. 

class Vector:
    def __init__(self, i, j, k):
        self.i = i
        self.j = j
        self.k = k
    
    def __add__(self, other):
        result = Vector(self.i + other.i, self.j + other.j, self.k + other.k)
        return result
    
    def __mul__(self, other):
        result =  self.i * other.i + self.j * other.j + self.k * other.k
        return result
    
    def __str__(self):
        return f"Vector({self.i}, {self.j}, {self.k})"

v1 = Vector(5, 3, 8)
v2 = Vector(7, 2, 4)
v3 = Vector(1, 6, 9)

# print(v1+v2)
# print(v1*v2)
# print(v1+v3)
# print(v1*v3)

# 6. Write __str__() method to print the vector as follows: 
#                                  7i + 8j +10k  
# Assume vector of dimension 3 for this problem. 

class Vector:
    def __init__(self, i, j, k):
        self.i = i
        self.j = j
        self.k = k

    def __str__(self):
        return f"{self.i}i + {self.j}j + {self.k}k"

c = Vector(7, 8, 10)
# print(c)

# 7. Override the __len__() method on vector of problem 5 to display the dimension of the vector.

class Vector:
    def __init__(self, l):
        self.l = l
    
    def __len__(self):
        return len(self.l)

v1 = Vector([5, 3, 8])
print(len(v1))
