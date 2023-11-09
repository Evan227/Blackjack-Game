import time

from gameplay.player import Player

from gameplay.probablity import Probability


class BlackJack: # implementing splitting a pair
    """
    class to generate the Blackjack game for the user
    """
    def __init__(self, shoe):
        """
        Blackjack constructor

        :param shoe: Shoe made from the Shoe class that takes in the input from the user of how large they want the Shoe to be
        """
        self.player = Player()
        self.dealer = Player()
        self.shoe = shoe
        self.probability = Probability(0)

    def start_game(self):
        """
        Starts the game of blackjack by giving the player and dealer their first 2 cards.

        :return: None
        """
        time.sleep(1)
        print("\nStarting a new game\n")
        first_player_card = self.shoe.pop()
        hidden_bot_card = self.shoe.pop()
        second_player_card = self.shoe.pop()
        revealed_bot_card = self.shoe.pop()

        self.probability.add_to_count(self.probability.card_count(first_player_card))
        self.probability.add_to_count(self.probability.card_count(second_player_card))
        self.probability.add_to_count(self.probability.card_count(revealed_bot_card))

        self.player.add(first_player_card)
        self.player.add(second_player_card)
        self.dealer.add(hidden_bot_card)
        self.dealer.add(revealed_bot_card)

        time.sleep(1)
        print("My revealed card is: " + revealed_bot_card.get_card() + "\n")

        time.sleep(1)
        print("Your first card: " + first_player_card.get_card())
        time.sleep(1)
        print("Your second card: " + second_player_card.get_card())
        time.sleep(1)
        print(f"Your total value is: {self.player.get_score()}")

    def hit(self, is_player):
        """
        Function to "hit" or draw another card to the deck

        :param is_player: True if the player hitting is the player and not the dealer
        :return: None
        """
        player_card = self.shoe.pop()

        if is_player:
            self.player.add(player_card)
        else:
            self.dealer.add(player_card)

        self.probability.add_to_count(self.probability.card_count(player_card))

        time.sleep(1)
        print("Your next card: " + player_card.get_card())

        score = 0

        if is_player:
            score = self.player.get_score()
        else:
            score = self.dealer.get_score()

        time.sleep(1)
        print(f"Total value is: {score}\n")

    def is_busted_or_blackjack(self, is_player):
        """
        Determines whether the Player has busted or gained blackjack. Effectively telling us when their turn has ended

        :param is_player: True if the player hitting is the player and not the dealer
        :return: True is the player has busted or got blackjack. False otherwise
        """
        score = 0

        if is_player:
            score = self.player.get_score()
        else:
            score = self.dealer.get_score()

        if score == 21:
            time.sleep(1)
            print("BLACKJACK")

            return True

        if score > 21:
            time.sleep(1)
            print("BUSTED\n")

            if is_player:
                self.player.reset_cards()
            else:
                self.dealer.reset_cards()

            return True

        return False

    def dealer_play(self):
        """
        Function used whenever the player turn ends. This function simulates when the dealer continually draws until
        they get a score of 16 or higher

        :return: None
        """
        time.sleep(1)
        print("\nMy Turn\n")

        hidden_card = self.dealer.cards[0]
        self.probability.add_to_count(self.probability.card_count(hidden_card))

        time.sleep(1)
        print("My hidden card was: " + hidden_card.get_card())

        time.sleep(1)
        print(f"My total value is {self.dealer.get_score()}")

        while not self.is_busted_or_blackjack(False):
            if self.dealer.get_score() >= 17: # TODO: implement that a dealer has to hit on a soft 16
                break

            self.hit(False)
            time.sleep(1)

        self.end_game()

    def end_game(self):
        """
        Determines the winner of the current hand

        :return: None
        """
        if self.player.get_score() > self.dealer.get_score():
            time.sleep(1)
            print("You Win\n")
        elif self.player.get_score() == self.dealer.get_score():
            time.sleep(1)
            print("Push\n")
        else:
            time.sleep(1)
            print("I win, you lose\n")

        self.player.reset_cards()
        self.dealer.reset_cards()

    def print_probability(self):
        """
        Prints the card count of the current shoe

        :return: None
        """
        time.sleep(1)
        print(f"\nCard count is: {self.probability.count}\n")
