from cards.card import Card

from cards.constants import (
    Suit,
    Cards
)


def create_deck():
    """
    function to create a deck of cards

    :return: full deck of cards
    """
    res = []

    for x in Suit:
        for y in Cards:
            hold = Card(x.value, y.name, y.value)
            res.append(hold)

    return res


class Deck:
    """
    class to simulate a Deck of cards
    """
    def __init__(self):
        """
        Deck constructor
        """
        self.deck = create_deck()

    def print_deck(self):
        """
        prints out all the cards in the deck

        :return: None
        """
        for x in self.deck:
            print(x.get_card())

    def get_deck(self):
        """
        gets the deck

        :return: the deck
        """
        return self.deck
