a = int(input("Please enter 'a': "))
b = int(input("Please enter 'b': "))
c = int(input("Please enter 'c': "))

if a + b == c:
    print('{}+{}={}'.format(a, b, c))
elif a + c == b:
    print('{}+{}={}'.format(a, c, b))
elif b + c == a:
    print('{}+{}={}'.format(b, c, a))
else:
    print("Wrong digits")