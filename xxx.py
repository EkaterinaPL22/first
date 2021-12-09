a = input("enter string:")

if a[:len("number")] == "number":
    if a[7:].isdigit():
        b = input("number")
        if b[7:].isdigit():
            print (int(a[7:]) + int(b[7:]))
        else:
            print ("wrong")
    elif a[7] == "-":
        if a[8:].isdigit():
            b = input("number")
            if b[8:].isdigit():
                print (int(a[7:]) + int(b[7:]))
            else:
                print ("wrong")
    else:
        print ("wrong")