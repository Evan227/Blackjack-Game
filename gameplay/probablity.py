import math


class Probability:
    def __init__(self, count):
        self.count = count

    def add_to_count(self, val):
        self.count += val

    def card_count(self, card):
        v = card.get_value()

        if v <= 6:
            return 1
        elif 7 <= v <= 9:
            return 0

        return -1
