import random

from card import Card


def create_deck():
    res = []

    suits = ["Diamonds", "Hearts", "Spades", "Clubs"]
    names = ["Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace"]
    vals = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]

    for x in suits:
        for y in range(len(names)):
            hold = Card(x, names[y], vals[y])
            res.append(hold)

    return res


class Deck:
    def __init__(self):
        self.deck = create_deck()

    def shuffle(self):
        return random.shuffle(self.deck)

    def print_deck(self):
        for x in self.deck:
            print(x.get_card())

    def get_deck(self):
        return self.deck
