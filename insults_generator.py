from random import randint

body_parts = ["twarz", "noga", "ręka", "pięta"]
adjectives = ['brzydsza', 'bardziej obsceniczna', 'szkaradniejsza', 'bardziej brudna']
animals = ['dzikiej kuny', 'czupakabry', 'dzikiego węża', 'bobra']


def generate(list):
    return list[randint(0, len(list) - 1)]

print('Your {} is {} than {} {}'.format(
    generate(body_parts),
    generate(adjectives),
    generate(body_parts),
    generate(animals)
))
