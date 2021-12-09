arr = ['moon', 45, 12, 'sky']
a_0 = []
a_1 = []
for i in arr:
    if type(i):
        a_0.append(i)
    else:
        a_1.append(i)
    a_0.sort()
    a_1.sort(key=len())
    with open (1.txt, 'a', encoding=utf-8):as f:
        for j in a_1:
            f.write(j)
        for n in a_0:
            f.write (n)

