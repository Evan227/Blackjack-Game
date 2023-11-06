import random

from cards.deck import Deck


def create_shoe(amount):
    res = []

    for x in range(amount):
        deck = Deck()
        res.extend(deck.deck)

    return res


class Shoe:
    def __init__(self, amount):
        self.shoe = create_shoe(amount)
        self.shuffle()

    def print_shoe(self):
        for x in self.shoe:
            print(x.get_card())

    def shuffle(self):
        random.shuffle(self.shoe)

    def get_shoe_size(self):
        return len(self.shoe)

    def peek(self):
        return self.shoe[0]

    def pop(self):
        return self.shoe.pop()
