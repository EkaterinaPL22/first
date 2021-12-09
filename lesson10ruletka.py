import random
players_count = int(input("vvedi kolichestvo igrokov:"))
players = []
for i in range(players_count):
    players.append(input(f"vvedi imy igroka{}:")) ####
copy_players = players.copy()
while True:
    bullet = random.randint(1,6)
    index = 0
    while len(copy_players) != 1:
        user_choice = int(input(f"{copy_players[index]}, viberi ot 1 do 6:"))
        if user_choice == bullet:
            print(f"{copy_players[index]} ymer")
            bullet = random.randint(1,6)
            del copy_players[index]
        else:
            print("povezlo")
            index *= 1
        if index > len(copy_players)-1:
            index = 0
    print(f"{copy_players[0]} pobeda")
    more = int(input("hotite esche poigrat? 1- da, 0- net:"))
    if not more:
        break
    elif more:
        copy_players = players.copy()
