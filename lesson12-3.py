a = [1, 2, 3]
index = int(input("enter:"))
b = input("xo")
try:
    a[index] = b
except IndexError:
    print("no index")