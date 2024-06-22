age = int(input("Enter your age: "))

# If else

if(age>=18):
    print("You are above the age of consent")
    print("Good for you")

else:
    print("You are below the age of consent")

print("End of program")

# If elif else ladder

# elif in python means [else if]. An if statements can be chained together with a lot of these elif statements followed by an else statement.

if(age>=18):
    print("You are above the age of consent")
    print("Good for you")

elif(age<=0):
    print("You are entering an invalid age")

else:
    print("You are below the age of consent")

print("End of program")
