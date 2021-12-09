a = [4,6,'py','tell',78]
b = [44, 'hello', 56,'exept', 3]
c = a+b
c.insert(3, 6)
for i in c:
    if type(i) is str:
        c.remove(i)
print(c)
print(len(c))
