from random import randint

zdania = [
    "Ok, niech będzie",
    "To nie jest najlepszy pomysł",
    "Może jutro",
    "To na pewno ból głowy",
    "Jak chcesz :P"
]

while True:
    print(zdania[randint(0, len(zdania) - 1)])
    print('')

    while True:
        losowac = input("Czy losować ponownie? [t/n] ")

        if losowac == 'n':
            exit(0)
        elif losowac == 't':
            break
        else:
            print("Nie rozumiem o co Ci chodzi :P")