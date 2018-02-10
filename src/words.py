import random

def gen():
    with open('words.txt') as file:
        words = set(file.readlines())
    while True:
        yield random.sample(words, 1)[0].strip()
