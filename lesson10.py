import random
a = [random.randint(0, 1520) for i in range(10)]
k = tuple(a)
print(k)
print('max', max(a), 'min', min(a))