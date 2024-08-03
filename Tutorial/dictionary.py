# Dictionary is a collection of keys-value pairs.

a = { 
    "key": "value", 
    "harry": "code", 
    "marks": "100", 
    "list": [1, 2, 9] 
} 
 
print(a["key"])  # Output: "value" 
print(a["list"])  # Output: [1, 2, 9] 

# PROPERTIES OF PYTHON DICTION ARIES  
# 1. It is unordered. 
# 2. It is mutable. 
# 3. It is indexed. 
# 4. Cannot contain duplicate keys

# a.items(): Returns a list of (key,value)tuples. 
# a.keys(): Returns a list containing dictionary's keys. 
# a.update({"friends":}): Updates the dictionary with supplied key-value pairs. 
# a.get("name"): Returns the value of the specified keys (and value is returned eg."harry" is returned here).
# More methods are available on docs.python.org 
marks = {
    "Shubham": 94,
    "Sohan": 84,
    "Rohan": 74,
}
print(marks["Shubham"])
print(len(marks))
print(marks.items())
print(marks.keys())
print(marks.values())
marks.update({"Rohan": 84})
print(marks)
print(marks.get("Shubham"))



# DICTIONARY MERGE & UPDATE  OPERATORS  
# New operators | and |= allow for merging and updating dictionaries. 
 
dict1 = {'a': 1, 'b': 2} 
dict2 = {'b': 3, 'c': 4} 
merged = dict1 | dict2 
print(merged)  # Output: {'a': 1, 'b': 3, 'c': 4}