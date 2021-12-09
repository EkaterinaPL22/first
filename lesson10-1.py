import random
a1 = tuple([random.randint(0, 5) for i in range(10)])
a2 = tuple([random.randint(-5, 0) for k in range(10)])
#b = tuple(a1)
#c = tuple(a2)
d = a1 + a2
print(d)
print(d.count(0))