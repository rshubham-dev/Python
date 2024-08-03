# Reduce applies a rolling computation to sequential pair of elements. 

from functools import reduce 
# val=reduce (function, list1)        
              # the function can be lambda function
l = [1, 2, 3, 4, 5]

def sum(a, b):
    return a + b 

print(reduce(sum, l))