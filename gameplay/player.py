class Player:
    def __init__(self):
        self.cards = []

    def add(self, card):
        self.cards.append(card)

    def reset_cards(self):
        self.cards = []

    def get_score(self):
        res = 0

        for c in self.cards:
            res += c.get_value()

        return res
