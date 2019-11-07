from random import randint

sentence = [
    "Ok, niech będzie",
    "To nie jest najlepszy pomysł",
    "Może jutro",
    "To na pewno ból głowy",
    "Jak chcesz :P"
]

while True:
    print(sentence[randint(0, len(sentence) - 1)])
    print('')

    while True:
        random = input("Whether to draw again? [y/n] ")

        if random == 'n':
            exit(0)
        elif random == 'y':
            break
        else:
            print("I don`t know what you mean :P")