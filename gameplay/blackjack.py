from gameplay.player import Player


class BlackJack:
    def __init__(self, shoe):
        self.player = Player(0)
        self.dealer = Player(0)
        self.shoe = shoe
        self.past_cards = []

    def start_game(self):
        first_player_card = self.shoe.pop()
        hidden_bot_card = self.shoe.pop()
        second_player_card = self.shoe.pop()
        revealed_bot_card = self.shoe.pop()

        self.past_cards.append(first_player_card)
        self.past_cards.append(hidden_bot_card)
        self.past_cards.append(second_player_card)
        self.past_cards.append(revealed_bot_card)

        self.player.add(first_player_card.get_value())
        self.player.add(second_player_card.get_value())
        self.dealer.add(hidden_bot_card.get_value())
        self.dealer.add(revealed_bot_card.get_value())

        print("My revealed card is: " + revealed_bot_card.get_card())

        print("Your first card: " + first_player_card.get_card())
        print("Your second card: " + second_player_card.get_card())
        print(f"Your total value is: {self.player.get_score()}")

    def hit(self):
        player_card = self.shoe.pop()

        self.player.add(player_card.get_value())
        self.past_cards.append(player_card)

        print("Your next card: " + player_card.get_card())

        score = self.player.get_score()

        print(f"Your total value is: {score}")

    def dealer_play(self):
        print("my other card is ")

