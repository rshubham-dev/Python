# THE GLOBAL KEYWORD  
# ‘global’ keyword is used to modify the variable outside of the current scope

a = 40

def func():
    global a
    a = 4
    print(a)

func()
print(a)