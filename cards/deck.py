from cards.card import Card

from cards.constants import (
    Suit,
    Cards
)


def create_deck():
    res = []

    for x in Suit:
        for y in Cards:
            hold = Card(x.value, y.name, y.value)
            res.append(hold)

    return res


class Deck:
    def __init__(self):
        self.deck = create_deck()

    def print_deck(self):
        for x in self.deck:
            print(x.get_card())

    def get_deck(self):
        return self.deck
