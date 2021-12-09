a = input("enter word:")
let_1 = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z']
let_2 = ['a', 'e', 'i', 'o', 'u', 'y']
sum_1 = 0  # согласные
sum_2 = 0  # гласные
for i in a:
    if i in let_1:
        sum_1 += 1
    else:
        sum_2 += 1
if sum_1 == sum_2:
    print(let_2)
print(sum_1, sum_2)