C_1 = (35, 78, 21, 37, 2, 98, 6, 100, 231)
C_2 = (45, 21, 124, 76, 5, 23, 91, 234)
a_1 = sum(C_1)
a_2 = sum(C_2)
print(a_1)
print(a_2)
if a_1 > a_2:
    print("a_1 bigger then a_2")
else:
    print("a_2 bigger then a_1")
print('min C_1 -', min(C_1), ';number - ', C_1.index(min(C_1)))
print('min C_2 -', min(C_2), ';number - ', C_2.index(min(C_2)))

