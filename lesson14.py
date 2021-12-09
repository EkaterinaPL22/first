import os

def privacy_to_file(name,surname, age, mob):
    with open("privacy.txt", 'a', encoding='utf-8') as f:
        privacy_id = os.stat("privacy.txt").st_size
        f.write(f'{privacy_id};{name},{surname},{age},{mob}\n')


def get_all_inf():
    privacy = {}
    with open ("privacy.txt", 'r', encoding='utf-8') as f:

        for line in f:
            line = line.replace("\n", "")
            line = line.split(":")
            privacy [line[0]] = {"name": line[1],
                                 "surname": line[2],
                                 "age": line[3],
                                 "mob": line[4]}
