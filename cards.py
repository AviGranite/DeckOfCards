import random
import itertools

suits = ('H', 'D', 'S', 'C')
digits = [str(i) for i in range(2, 11)]
face = ['Jack', 'Queen', 'King']
values = digits + face + ['Ace']
deck = []

for i in suits:
    deck.extend(list(zip(values, itertools.repeat(i))))

random.shuffle(deck) #shuffle
#print(deck)
deck_g = (c for c in deck) #deck as a generator
