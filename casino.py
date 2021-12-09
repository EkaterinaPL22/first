import random
num = random.randint(1, 10)
col = random.randint(1, 2) # 1red 2black
print(num)
print(col)
i = 0
while i < 5:
    i += 1
    guess = int(input("your number:"))
    color = int(input("color: 1 red or 2 black:"))
    if guess > num:
        print("number less then your")
        if color == col:
            print("your color right")
        else:
            print("you dont right")
    elif guess < num:
        print("number bigger then your")
        if color == col:
            print("your color right")
        else:
            print("you dont right")
    elif guess == num and col != color:
        print("no color, but number")
    elif guess == num and col == color:
        print("congrats!", num, col)
        break
    if i < 5:
        print("try more")
    else:
        print("it was numb", num, col, "game over")







