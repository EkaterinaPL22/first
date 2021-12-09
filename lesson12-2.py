# while True:
#     try:
#         age = int(input("how old are you?:"))
#     except ValueError:
#         print("repeat age")
#     else:
#         if age >= 18:
#             print("beer")
#         elif age < 18 and age > 0:
#             print("cola")
#         else:
#             print("liar")
#         break

a = 1
b = 9
c = 0
for i in range(a,b):
    if i % 3 == 0:
        del i
    try:
        c += i ** 2
        print(c)
    except NameError:
        print("mistake")


