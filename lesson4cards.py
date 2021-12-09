a = float(input("on card:"))
i = float(input("spend:"))
s = 0
while i < a:
      a -= i
      s += 1
      i = float(input("spend"))
print(a)
print("amount", s)