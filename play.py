wins = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
player_x = []
player_o = []
max = 9 # максимальное кол-во ходов
while max >= 1:
    x = int(input("enter 1-9:"))
    while x in player_x or x in player_o:
        x = int(input("enter 1-9:"))
    player_x.append(x)

    # for k in wins:  # k = [1, 2, 3]
    #     for j in k:  # j = 1 2 3
    #         if j in player_x:

    max -= 1
    if max == 0:
        print("non") # ничья

    y = int(input("enter 1-9:"))
    while y in player_o or y in player_x:
        y = int(input("enter 1-9:"))
    player_o.append(y)
    max -= 1

    if max == 0:
        print("non") # ничья
