# Set is a collection of non-repetitive elements.

e = set()           # no repetition allowed! 
e.add(1) 
e.add(2)           # or set ={1,2} 

# PROPERTIES OF SETS  
# 1. Sets are unordered => Element’s order doesn’t matter 
# 2. Sets are unindexed => Cannot access elements by index 
# 3. There is no way to change items in sets. 
# 4. Sets cannot contain duplicate values. 

# OPERATIONS ON SETS  

s = {1,8,2,3} 
print(len(s)) # Returns 4, the length of the set  
s.remove(8) # Updates the set s and removes 8 from s.
print(s)  
print(s.pop()) # Removes an arbitrary element from the set and return the element removed.
s.clear() # empties the set s.
print(s)  
print(s.union({8,11})) # Returns a new set with all items from both sets. {1,8,2,3,11}. 
print(s.intersection({8,11})) # Return a set which contains only item in both sets {8}.