# Q1) 
name = input("Enter your name: ")
print("Good Afternoon", name)
print(f"Good Afternoon {name}") # f string to use variable

# Q2) 
letter = '''  
       Dear <|Name|>, 
       You are selected! 
       <|Date|> 
        '''

print(letter.replace("<|Name|>", "Shubham").replace("<|Date|>", "24 Feb 2030"))

# Q3) 
Name = "Shubham  is  a good boy  and "
print(Name.find(" "))

# Q4) 
print(Name.replace("  ", " "))

# Q5)
letter = "Dear Harry, \n\tThis python course is nice. \nThanks!"
print(letter)