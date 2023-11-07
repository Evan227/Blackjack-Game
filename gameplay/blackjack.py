import time

from gameplay.player import Player


class BlackJack:
    def __init__(self, shoe):
        self.player = Player()
        self.dealer = Player()
        self.shoe = shoe
        self.past_cards = []

    def start_game(self):
        print("\nStarting a new game\n")
        first_player_card = self.shoe.pop()
        hidden_bot_card = self.shoe.pop()
        second_player_card = self.shoe.pop()
        revealed_bot_card = self.shoe.pop()

        self.past_cards.append(first_player_card)
        self.past_cards.append(hidden_bot_card)
        self.past_cards.append(second_player_card)
        self.past_cards.append(revealed_bot_card)

        self.player.add(first_player_card)
        self.player.add(second_player_card)
        self.dealer.add(hidden_bot_card)
        self.dealer.add(revealed_bot_card)

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

        self.past_cards.append(player_card)

        time.sleep(1)
        print("Your next card: " + player_card.get_card())

        score = 0

        if is_player:
            score = self.player.get_score()
        else:
            score = self.dealer.get_score()

        time.sleep(1)
        print(f"Total value is: {score}\n")

        if score == 21:
            time.sleep(1)
            print("BLACKJACK")

            if is_player:
                self.dealer_play()

    def is_busted(self, is_player):
        score = 0

        if is_player:
            score = self.player.get_score()
        else:
            score = self.dealer.get_score()

        if score > 21:
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

        while not self.is_busted(False):
            if self.dealer.get_score() >= 17:
                break

            self.hit(False)
            time.sleep(1)

        self.end_game()

    def end_game(self):
        if self.player.get_score() > self.dealer.get_score():
            print("You Win\n")
        elif self.player.get_score() == self.dealer.get_score():
            print("Push\n")
        else:
            print("I win, you lose\n")

        self.player.reset_cards()
        self.dealer.reset_cards()
