num_1 = int(input("enter first number:"))
num_2 = int(input("enter second number:"))
while (num_1 < 0 or num_2 < 0) and (num_1 <= num_2):
    print(num_1)
    num_1 += 1
