#a = input("enter numbers").split()
#print(sum(a.count(x) - 1 for x in a) // 2)



a = [1, 3, 4, 1, 3, 8, 8]
couples = dict.fromkeys(set(a), 0)
for i in enumerate(a):
    for j in a[i[0]+1:]:
        if j == i[1]:
            couples [i[1]] += 1
print(couples)
#for key, value in dict.items():
    #if value != 0:
        #print(f'{key} - {value} couples')





