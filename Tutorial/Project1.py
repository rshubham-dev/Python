import random
'''
snake = 1,
water = -1, 
gun = 0,
'''

computer = random.choice([-1, 0, 1])
youInp = input("Enter your choice:")
youDict = {"s": 1, "w": -1, "g": 0}
reverseDict = {1: "s", -1: "w", 0: "g"}
you = youDict[youInp]
print(f"You chose {reverseDict[you]}\n Computer chose {reverseDict[computer]}")

if(computer == you):
    print('Its a Draw')
else:
    if(computer == -1 and you == 1): # -2
        print("You Win!")
    elif(computer == 1 and you == -1): # 2
        print("Computer Win!")
    elif(computer == -1 and you == 0): # -1
        print("Computer Win!")
    elif(computer == 1 and you == 0): # 1
        print("You Win!")
    elif(computer == 0 and you == 1): # -1
        print("Computer Win!")
    elif(computer == 0 and you == -1): # 1
        print("You Win!")
    else:
        print("Something went wrong!")

# Second approach
# if(computer == you):
#     print('Its a Draw')
# else:
#     if((computer - you) == -2 or (computer - you) == 1):
#         print("You Win!")
#     else:
#         print("Computer Win!")