import random
numbers_count = int(input("vvedi kolichestvo randomnih chisel:"))
number = input("vvedi chislo kotoroe nado iskat:")
count = 0
for i in range(numbers_count):
    random_number = str(random.randint(1,1000))
    for j in random_number:
        if number == j:
            count += 1
    print(random_number)
print(count)








