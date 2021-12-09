a = input("enter string:")
if a[:len("number")] == "number":
    if a[7:].isdigit():
        b = input("number")
        if b[7:].isdigit():
            print (int(a[7:])+int(b[7:]))
        else:
            print ("wrong")
    else:
        print ("wrong")
elif a[:len("string")] == "string":
    print (a[7:]*3)
elif a == "true":
    print ("you right")
elif a == "false":
    print ("not right")
else:
    print ("wrong")
