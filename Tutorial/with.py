# The best way to open and close the file automatically is the with statement. 
# Open the file in read mode using 'with', which automatically closes the file 
with open("text.txt", "r") as f: 
    # Read the contents of the file 
    text = f.read() 
 
# Print the contents 
print(text) 


# You can now use multiple context managers in a single with statement more cleanly using the parenthesised context manager 

with ( 
    open('file1.txt') as f1, 
    open('file2.txt') as f2 
): 
    text = f1.read()
    # Process files