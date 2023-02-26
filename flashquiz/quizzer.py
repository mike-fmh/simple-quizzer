from flashquiz.flashcards.deck import Deck
from flashquiz.args import handle_args
from flashquiz.gui import GUI


def main():
    args = handle_args()
    GUI(args).init_screen()


if __name__ == '__main__':
    d = Deck()

    d.add_card("hello", "world")
    d.print()
    print("\n")

    main()
    while True:
        pass
