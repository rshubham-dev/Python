# 1. Write a program using functions to find greatest of three numbers. 
# 2. Write a python program using function to convert Celsius to Fahrenheit. 
# 3. How do you prevent a python print() function to print a new line at the end. 
# 4. Write a recursive function to calculate the sum of first n natural numbers. 
# 5. Write a python function to print first n lines of the following pattern: 
# *** 
# **               - for n = 3 
# * 
 
# 6. Write a python function which converts inches to cms. 
# 7. Write a python function to remove a given word from a list and strip it at the same time. 
# 8. Write a python function to print multiplication table of a given number.


# Q1)

# def gratest(n1, n2, n3):
#     if(n1>n2 and n1>n3):
#         return n1
#     elif(n2>n1 and n2>n3):
#         return n2
#     elif(n3>n2 and n3>n1):
#         return n3
# n1 = int(input("Enter number 1: "))
# n2 = int(input("Enter number 2: "))
# n3 = int(input("Enter number 3: "))
# print(f"Gratest number is {gratest(n1, n2, n3)}")

# Q2) 
# f = int(input("Enter temperature in F: "))
# def tempconverter(f):
#     return 5*(f-32)/9

# print(f"{round(tempconverter(f), 2)} Degree C")

# Q3)
# print("a")
# print("b", end="")
# print("c")
# print("d", end="")

# Q4)

# def sum(n):
#     if(n==1):
#         return 1
#     if(n>=0):
#         return sum(n-1) + n
#     else:
#         return "Invalid input"
    
# n = int(input("Enter number: "))
# print(f"Sum of first natural number is {sum(n)}")

# Q5)
# def pattern(n):
#     if(n==0):
#         return
#     print("*" * n)
#     pattern(n-1)

# n = int(input("Enter number: "))

# Q6)
# def inch_to_cm(inch):
#     return inch * 2.54

# inch = int(input("Enter inch: "))
# print(f"Inch to Cm {inch_to_cm(inch)}")

# Q7)
# def rem(l, word):
#     n = []
#     for item in l:
#         if not(item == word):
#             n.append(item.strip(word))
#             return n
#         l.remove(word)
#         return l

# l = ["Shubham", "Harry", "Rohan", "hi", "By"]
# word = input("Enter the word to be removed: ")
# print(rem(l, word))

# Q8)
# def multiplication(n):
#     if(n==0):
#         return
#     for i in range(1, 11):
#         print(f"{n} X {i} = {n * i}")

# n = int(input("Enter number: "))
# multiplication(n)