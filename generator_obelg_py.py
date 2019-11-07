from random import randint

body_parts = ["twarz", "noga", "ręka", "pięta"]
adjectives = ['brzydsza', 'bardziej obsceniczna', 'szkaradniejsza', 'bardziej brudna']
animals = ['dzikiej kuny', 'czupakabry', 'dzikiego węża', 'bobra']


def losuj(lista):
    return lista[randint(0, len(lista) - 1)]

print('Twoja {} jest {} niż {} {}'.format(
    losuj(body_parts),
    losuj(adjectives),
    losuj(body_parts),
    losuj(animals)
))
