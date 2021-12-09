a = 7
guess = int(input("Try to guess a number: "))

while a != guess:
    print("You lose")
    guess = int(input("Try to guess a number: "))

print("Good job")
