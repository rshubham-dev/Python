# EXCEPTION HANDLING IN PYTHON  
# There are many built-in exceptions which are raised in python when something goes wrong. 
# Exception in python can be handled using a try statement. The code that handles the exception is written in the except clause. 

# try: 
   # Code which might throw exception  
# except Exception as e:  
#     print(e) 

try:
    a = int(input("Hey, Enter a number: "))
    print(a)
except Exception as e:
    print(e)
    

# When the exception is handled, the code flow continues without program interruption. 

# We can also specify the exception to catch like below:
 
# try: 
    # Code 
# except ZeroDivisionError: 
    # Code 
# except TypeError: 
    # Code 
# except: 
    # Code       # All other exceptions are handled here. 


# RAISING EXCEPTIONS 
# We can raise custom exceptions using the ‘raise’ keyword in python.

a = int(input("Hey, Enter a number: "))
b = int(input("Hey, Enter second number: "))

if(b == 0):
    raise ZeroDivisionError("Hey aour program is not meant to divide numbers by zero")
else:
    print(f"The division a/b is {a/b}")

 

