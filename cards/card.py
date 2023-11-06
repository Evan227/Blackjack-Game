class Card:
    def __init__(self, suit, name, value):
        self.suit = suit
        self.name = name
        self.value = value

    def get_suit(self):
        return self.suit

    def get_name(self):
        return self.name

    def get_value(self):
        return self.value

    def get_card(self):
        return f"{self.name} of {self.suit}"