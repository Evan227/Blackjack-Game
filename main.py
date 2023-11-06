from cards.shoe import Shoe

from gameplay.blackjack import BlackJack


def main():
    amount_of_decks = input("How many decks do you want in the shoe?\n")

    if not amount_of_decks.isnumeric():
        raise Exception("input must be a number")

    shoe = Shoe(int(amount_of_decks))

    blackjack = BlackJack(shoe)

    active = True

    first_turn = True

    while active:
        if first_turn:
            blackjack.start_game()
            first_turn = False

        user_input = input("press h to hit, s to stand, p for probabilities (card count, probability "
                           "of next card being 10, etc.), q to quit\n")

        match user_input:
            case 'h':
                blackjack.hit()
            case 's':
                print('hold')
            case 'p':
                print('hold')
            case 'q':
                active = False
                first_turn = True
                continue


main()
