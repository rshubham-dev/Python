# LIST COMPREHENSIONS  
# List Comprehension is an elegant way to create lists based on existing lists. 

list1 = [1,7,12,11,22]

# squaredList = []
# for item in list1:
#      squaredList.append(item*item)

# print(squaredList)

# This can be simplified using list comprehension
squaredList = [i*i for i in list1]
print(squaredList)