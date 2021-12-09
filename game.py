import random
#1=stone
#2=scissors
#3=paper
a = random.randint(1, 3)
b = int(input("enter number:"))
if  (a == 1 and b == 3) or (a == 2 and b == 1) or (a == 3 and b == 2):
    print("vinner")
elif a == b:
    print("lucky")
else:
    print("lose")