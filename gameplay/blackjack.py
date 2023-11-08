import time

from gameplay.player import Player

from gameplay.probablity import Probability


class BlackJack:
    def __init__(self, shoe):
        self.player = Player()
        self.dealer = Player()
        self.shoe = shoe
        self.probability = Probability(0)

    def start_game(self):
        time.sleep(1)
        print("\nStarting a new game\n")
        first_player_card = self.shoe.pop()
        hidden_bot_card = self.shoe.pop()
        second_player_card = self.shoe.pop()
        revealed_bot_card = self.shoe.pop()

        self.probability.add_to_count(self.probability.card_count(first_player_card))
        self.probability.add_to_count(self.probability.card_count(hidden_bot_card))
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
        time.sleep(1)
        print("\nMy Turn\n")

        hidden_card = self.dealer.cards[0]

        time.sleep(1)
        print("My hidden card was: " + hidden_card.get_card())

        time.sleep(1)
        print(f"My total value is {self.dealer.get_score()}")

        while not self.is_busted_or_blackjack(False):
            if self.dealer.get_score() >= 17:
                break

            self.hit(False)
            time.sleep(1)

        self.end_game()

    def end_game(self):
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
        time.sleep(1)
        print(f"\nCard count is: {self.probability.count}\n")
