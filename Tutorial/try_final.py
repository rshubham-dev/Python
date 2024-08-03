# TRY WITH FINALLY  
# Python offers a ‘finally’ clause which ensures execution of a piece of code inspective of the exception. 
 
try: 
    a = int(input("Hey, Enter a number: "))
    print(a)

except Exception as e: 
    print(e)

finally: 
    print("I am inside finally") # Executed regardless of error!