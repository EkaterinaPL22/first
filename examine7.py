a = [0, 1, 2, 3]
index = int(input("enter:"))
b = input("more")
try:
    a[index] = b
except IndexError:
    print("no find")