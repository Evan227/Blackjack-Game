from cards.constants import Cards

class Player:
    """
    class to simulate a player in the blackjack game
    """
    def __init__(self):
        """
        Player constructor, possesses a cards list that keeps track of the players current hand
        """
        self.cards = []

    def add(self, card):
        """
        Adds a card to the player's hand

        :param card: Card to add to player's hand
        :return: None
        """
        self.cards.append(card)

    def reset_cards(self):
        """
        Resets the current hand at the beginning of a turn

        :return: None
        """
        self.cards = []

    def get_score(self):
        """
        Gets the score of the player's current hand

        :return: Score of current player's hand
        """
        res = 0

        has_ace = False

        for c in self.cards:
            if c.get_name() == "Ace":
                has_ace = True

            if has_ace and c.get_name == Cards.Ace.name and res > 21:
                res -= 10

            res += c.get_value()

        return res
