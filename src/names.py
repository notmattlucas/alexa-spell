import random

def gen():
    with open('nouns.txt') as file:
        nouns = set(file.readlines())
    with open('adjectives.txt') as file:
        adjectives = set(file.readlines())
    while True:
        noun = random.sample(nouns, 1)[0].strip()
        adjective = random.sample(adjectives, 1)[0].strip()
        yield "%s %s" % (adjective, noun)
