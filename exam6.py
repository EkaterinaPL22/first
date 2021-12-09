stroka = input("vvedi stroky:")
lower = 0
upper = 0
for i in enumerate(stroka):
    if i == len(stroka) - 1:
        break
    if i[1].islower() and stroka[i[0]+1].islower():
        lower += 1
    elif i[1].isupper() and stroka[i[0]+1].isupper():
        upper += 1
    else:
        break
print(lower) #вывести пары
print(upper)