# 1. Write a program to print multiplication table of a given number using for loop. 
# 2. Write a program to greet all the person names stored in a list ‘l’ and which starts with S. l = ["Harry", "Soham", "Sachin", "Rahul"] 
# 3. Attempt problem 1 using while loop. 
# 4. Write a program to find whether a given number is prime or not. 
# 5. Write a program to find the sum of first n natural numbers using while loop. 
# 6. Write a program to calculate the factorial of a given number using for loop. 
# 7. Write a program to print the following star pattern. 
#    * 
#  *** 
# *****  for n = 3 
# 8. Write a program to print the following star pattern: 
# * 
# ** 
# ***      for n = 3 
# 9. Write a program to print the following star pattern. 
# * * * 
# *    *    for n = 3 
# * * *  
# 10. Write a program to print multiplication table of n using for loops in reversed 
# order.


# Q1)

n = int(input("Enter a number: "))

# for i in range(1, 11):
#     print(f"{n} X {i} = {n * i}")

# Q2)
# l = ["Harry", "Soham", "Sachin", "Rahul"]

# for name in l:
#     if(name.startswith("S")):
#         print(f"Hello {name}")

# Q3)

# i = 1
# while(i<11):
#     print(f"{n} X {i} = {n * i}")
#     i += 1

# Q4)

# for i in range(2, n):
#     if(n%i) == 0:
#         print("Number is not prime")
#         break
# else:
#     print("Number is prime")

# Q5) 

# i = 1
# sum = 0
# while(i<=n):
#     sum += i
#     i+=1

# print(sum)

# Q6)

# product = 1
# for i in range(1, n+1):
#     product = product * i

# print(f"The factorial of {n} is {product}")

# Q7)
# for i in range(1, n+1):
#     print(" "*(n-i), end="")
#     print("*"*(2*i-1), end="")
#     print("\n")

# Q8)
# for i in range(1, n+1):
#     print("*"*(2*i-1), end="")
#     print("\n")

# Q9) 
# for i in range(1, n+1):
#     if(i==1 or i==n):
#         print("*"*n, end="")
#     else:
#         print("*", end="")
#         print(" "*(n-2), end="")
#         print("*", end="")
#     print("")