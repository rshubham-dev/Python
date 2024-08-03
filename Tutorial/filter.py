# Filter creates a list of items for which the function returns true. 

# list(filter(function)) 
              # the function can be lambda function
l = [1, 2, 3, 4, 5]

def even(n):
    if(n%2 == 0):
        return True
    return False

onlyEven = filter(even, l)
print(list(onlyEven))