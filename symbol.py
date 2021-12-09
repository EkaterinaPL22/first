a = input("enter name:")
b = input("choose symbol:")
c = ''
for i in a:
    if i != b:
        c += i
print ("result:", c)