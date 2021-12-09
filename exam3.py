import random
user_number_1= int(input("vvedi pervoe chislo:"))
user_number_2 = int(input("vvedi vtoroe chislo:"))
rand = 0
user = 0
equal = 0
iter4_1 = 0
iter4_2 = 0
for i in range(9):
    random_number_1 = random.randint(1,20)
    random_number_2 = random.randint(1, 20)
    if i == 4:
        iter4_1 = random_number_1
        iter4_2 = random_number_2
    if user_number_1+user_number_2 > random_number_1+random_number_2:
        user += 1
    elif user_number_1+user_number_2 < random_number_1+random_number_2:
        rand += 1
    else:
        equal += 1
if user == rand and equal == rand:
    print(f"{iter4_1}{iter4_2}")