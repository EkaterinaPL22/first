a = input("1, 2, 3, 4, 4, 5")
b = input("1, 2, 4, 6, 8, 9, 1")
a_set = set(a)
b_set = set(b)
c = a_set & b_set
print(c)
d = a_set - b_set