import random

a = [random.randint(0, 25) for i in range(4)]
if 20 in a:
    a[a.index(20)] = 200
print(a)



