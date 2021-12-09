line = [15, 48, 'hello', 6, 19, 'world']
let_1 = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z']
let_2 = ['a', 'e', 'i', 'o', 'u', 'y']
sum_1 = 0  # согласные
sum_2 = 0  # гласные
for i in line:
    if type(i) is int:
        if i % 2 == 0:
            k = str(i)
            plus = 0
            for j in k:
                j = int(j)
                plus += j
            print(plus)
        else:
            line[line.index(i)] = 1
    elif type(i) is str:
        for v in i:
            if v in let_1:
                sum_1 += 1
            else:
                sum_2 += 1
print(line)
print(sum_1, sum_2)













