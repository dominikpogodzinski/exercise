from random import randint

czesci_ciala = ["twarz", "noga", "ręka", "pięta"]
przymiotniki = ['brzydsza', 'bardziej obsceniczna', 'szkaradniejsza', 'bardziej brudna']
zwierzeta = ['dzikiej kuny', 'czupakabry', 'dzikiego węża', 'bobra']


def losuj(lista):
    return lista[randint(0, len(lista) - 1)]

print('Twoja {} jest {} niż {} {}'.format(
    losuj(czesci_ciala),
    losuj(przymiotniki),
    losuj(czesci_ciala),
    losuj(zwierzeta)
))
