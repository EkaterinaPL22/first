import random
a = input("Welcome to Bank! Whats your name?:")
card = [random.randint(1,9) for i in range(16)]
print(f"your card {card}")       #k = ','.join(card)
cvv = [random.randint(1,9) for k in range(3)]
print(f"your cvc_cod {cvv}")
card_date = int(input("enter the year now:"))
print(f"card_valid {card_date+4}")
curr = int(input("choose_currency\n1-USD\n2-EUR\n3-RUB\n4-BYN"))
if curr == 1 or 2 or 3 or 4:
    print(f'ok, your card in {curr}') #curr?
sum_card = ([random.randint(0,10000) for i in range(1)])
print(f"on card this sum {sum_card}")  #without[]
#incom = sum_card + int
#print("incom:")
#shoping = sum_card - int
#print("shoping:")



