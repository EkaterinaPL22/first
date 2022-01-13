def card_hide(card):
    return '*' * len(card[:-4]) + card[-4:]


print(card_hide("1111222233334444"))


