# ENUMERATE FUNCTION IN PYTHON  
# The ‘enumerate’ function adds counter to an iterable and returns it 
l = [3, 85, 855, 964, 54]

# index = 0
# for item in l: 
#     print(f"the item number at index {index} is {item}")
#     index += 1 

# This can be simplified using enumerate function

for index, item in enumerate(l): 
    print(f"the item number at index {index} is {item}")  # Prints the items of list 1 with index