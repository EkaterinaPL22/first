f = open("test.txt", "r")
j = f.readline()
#j = j.split() разбивает
k = 0
for i in j:
    if i.isdigit():
        k += int(i)
print(k)


