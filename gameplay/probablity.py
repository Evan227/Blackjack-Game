import math


class Probability:
    """
    class to generate different probablities and card count of current deck
    """
    def __init__(self, count):
        """
        Probability constructor

        :param count: the card count of the shoe
        """
        self.count = count

    def add_to_count(self, val):
        """
        Add to the card count of the shoe

        :param val: value to add to the card count
        :return: None
        """
        self.count += val

    def card_count(self, card):
        """
        Gets the card count of the input card to know if we need to add or subtract from the total card count

        :param card: Card to assess
        :return: Card count of card
        """
        v = card.get_value()

        if v <= 6:
            return 1
        elif 7 <= v <= 9:
            return 0

        return -1
