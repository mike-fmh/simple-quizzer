from flashquiz.flashcards.parser import from_csv
from flashquiz.args import handle_args
from flashquiz.gui import GUI


def main():
    args = handle_args()
    GUI(args).init_screen()
    deck = from_csv(args.file)
    deck.print()


if __name__ == '__main__':
    main()
    while True:
        pass
