long_word = ('t', 't', 'a', 'u', 'u', 'a', 'u', 'u', 'u', 't', 't', 'a', 'u', 'u', 'u', 'u', 'u', 't', 'u', 'l')
letters = []
for i in long_word:
    if i in letters:
        continue
    else:
        print(f"{i}-{long_word.count(i)}")
        letters.append(i)

