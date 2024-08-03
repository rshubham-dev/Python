# FORMAT METHOD (STRINGS)  
# Formats the values inside the string into a desired output. 
# template.format(p1,p2...) 
# Syntax: 
a = "{1} is a good {0}".format("harry", "boy")   #1. 
b = "{0} is a good {1}".format("harry", "boy")  #2. 

print(a)
print(b)
 
# output for 1: 
# harry is a good boy  
 
# output for 2: 
# boy is a good harry 