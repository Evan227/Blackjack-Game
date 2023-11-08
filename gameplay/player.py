class Player:
    def __init__(self):
        self.cards = []

    def add(self, card):
        self.cards.append(card)

    def reset_cards(self):
        self.cards = []

    def get_score(self):
        res = 0

        has_ace = False

        for c in self.cards:
            if c.get_name() == "Ace":
                has_ace = True

            res += c.get_value()

        if res > 21 and has_ace:
            res -= 10

        return res
