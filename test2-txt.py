f = open("test2.txt", "r")
b = []
n = []
s = f.readlines()
print(s)
for i in s:
    i = i[:-1]
    if i.isalpha():
        i = str(i)
        b.append(i)
    elif i.isdigit():
        i = int(i)
        n.append(i)
print(b)
print(n)
n.sort()
b.sort()
#mas = n + b
#print(mas)







