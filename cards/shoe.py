import random

from cards.deck import Deck


def create_shoe(amount):
    """
    Creates a shoe of the amount of decks given. A shoe is just a collection of decks

    :param amount: the amount of decks to be added to the shoe
    :return: the list of all cards in the shoe
    """
    res = []

    for x in range(amount):
        deck = Deck()
        res.extend(deck.deck)

    return res


class Shoe:
    """
    Class to simulate a shoe of decks of cards
    """
    def __init__(self, amount):
        """
        Shoe constructor

        :param amount: amount of decks to add to the shoe
        """
        self.shoe = create_shoe(amount)
        self.shuffle()

    def print_shoe(self):
        """
        prints out all the cards in the shoe

        :return: None
        """
        for x in self.shoe:
            print(x.get_card())

    def shuffle(self):
        """
        Shuffles the cards in the shoe

        :return: None
        """
        random.shuffle(self.shoe)

    def get_shoe_size(self):
        """
        Gets the size of the shoe

        :return: size of shoe
        """
        return len(self.shoe)

    def peek(self):
        """
        gets the first card of the shoe

        :return: first card of the shoe
        """
        return self.shoe[0]

    def pop(self):
        """
        gets the first card of the shoe and removes it from the shoe

        :return: first card of the shoe
        """
        return self.shoe.pop()
