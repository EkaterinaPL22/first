a = {'book': ['12$', 5]}
card = {}
for key, value in a.items():
    print((f'{key}-{value[0]} {value[1]}'))
while True:
    user = input("1-buy, n-out")
    if user == "1":
        b = input("...")
        if b in a.keys():
            c = input("...")
            if c>a[b][1]:
                print("no")
            else:
                card[b] = c
                a[b][c] -= c
        elif user =="n":
            for key.value in card.items:
                print(f'{key}-{value}-{a[key][0]*value}')
                break




