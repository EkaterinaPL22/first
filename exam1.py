a = input("enter 7long number:")
count_1 = 0
count_2 = 0
for i in a:
    if int(i) % 2 == 0:
        count_1 += 1
    else:
        count_2 += 1
print("chetnie: ", count_1, "nechetnie: ", count_2)
sum_1 = 0
pr = 1
if count_1 > count_2:
    for i in a:
        sum_1 += int(i)
    print("the sum: ", sum_1)
else:
    pr = int(a[0])*int(a[2])*int(a[5])
    print("the pr: ", pr)





