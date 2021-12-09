b = []
a = [5, 5, 5, 3, 6, 6, 9]
for i in a:
   k = 0
   for j in a:
      if i == j:
         k += 1
   if k > 2:
      b.append(i)
print(set(b))

