name = input("what is your name:")
while True:
    mail = input("enter email:")
    if '@' in mail:
        if '.' in mail[mail.index('@'):]:
            break
        else:
            print("email not right")
    else:
        print("email not right")
while True:
    phone = input("enter mob number:")
    if phone[:4] == "+375":
        if phone[1:].isdigit():
            if len(phone) == 13:
                break
print("ciao")
            #else:
                #pass
        #else:
            #pass
    #else:
        #pass




