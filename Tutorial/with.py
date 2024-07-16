# The best way to open and close the file automatically is the with statement. 
# Open the file in read mode using 'with', which automatically closes the file 
with open("text.txt", "r") as f: 
    # Read the contents of the file 
    text = f.read() 
 
# Print the contents 
print(text) 