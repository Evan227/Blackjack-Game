class Card:
    """
    class to simulate a Card in a Deck of Cards
    """
    def __init__(self, suit, name, value):
        """
        Card constructor

        :param suit: Suit of the card (Diamonds, Spades, etc)
        :param name: Name of the card (Two, Three, etc)
        :param value: What the card is worth (Two = 2, Three = 3, etc)
        """
        self.suit = suit
        self.name = name
        self.value = value

    def get_suit(self):
        """
        gets suit of the card

        :return: suit of card
        """
        return self.suit

    def get_name(self):
        """
        gets name of the card

        :return: name of card
        """
        return self.name

    def get_value(self):
        """
        gets value of the card

        :return: value of card
        """
        return self.value

    def get_card(self):
        """
        gets the suit and name of the card

        :return: name and suit of card
        """
        return f"{self.name} of {self.suit}"
