# CHAPTER 13 - PRACTICE SET  
# 1. Create two virtual environments, install few packages in the first one. How do you create a similar environment in the second one? 

# 2. Write a program to input name, marks and phone number of a student and format it using the format function like below: 
# “The name of the student is Harry, his marks are 72 and phone number is 99999888” 

# name = input("Enter name: ")
# marks = int(input("Enter marks: "))
# phone = int(input("Enter number: "))

# s = "The name of the student is {}, his marks are {} and phone number is {}".format(name, marks, phone)

# print(s)

# 3. A list contains the multiplication table of 7. write a program to convert it to vertical string of same numbers. 

table = [str(7*i) for i in range(1, 11)]
s = "\n".join(table)
# print(s)
                                                       
# 4. Write a program to filter a list of numbers which are divisible by 5.

def divisible5(n):
    if(n%5 == 0):
        return True
    return False

a = [1, 5, 56, 452, 40, 25, 80, 70, 6546, 786, 56]
f = list(filter(divisible5, a))
# print(f)
 
# 5. Write a program to find the maximum of the numbers in a list using the reduce function. 
from functools import reduce
l = [1, 5455, 56546, 452, 46460, 2568746, 805475, 4570, 6546, 786, 568796]

def maxno(a, b):
    if(a>b):
        return a
    return b
# print(reduce(maxno, l))

# 6. Run pip freeze for the system interpreter. Take the contents and create a similar virtualenv. 


# 7. Explore the ‘Flask’ module and create a web server using Flask & Python.