# A for loop is used to iterate through a sequence like list, tuple, or string [iterables]

l = [1, 687, 32, 65, 68, 53, 50]
for item in l:
    print(item)

# The range() function in python is used to generate a sequence of number. 
# We can also specify the start, stop and step-size as follows:

# range(start, stop, step_size) 
# step_size is usually not used with range()

for i in range(0,7): # range(7) can also be used. 
    print(i) # prints 0 to 6 

t = (546, 32, 87, 54)
for i in t:
    print(i)


s = "Shubham"
for i in s:
    print(i)

for item in l:
    print(item)
else:
    print("done")

# ‘break’ is used to come out of the loop when encountered. It instructs the program to – exit the loop now. 

for i in range (40):
    if(i == 33):
        break # Exit the loop right now
    print(i)

# continue’ is used to stop the current iteration of the loop and continue with the next one. It instructs the Program to “skip this iteration”.

for i in range (40):
    if(i == 33):
        continue # Skip the iteration
    print(i)

# pass is a null statement in python. 
# It instructs to “do nothing”

for i in range(400):
    pass


i = 0
while(i<45):
    print(i)
    i += 1