from flashquiz.flashcards.parser import from_csv
from flashquiz.args import handle_args
from flashquiz.gui import GUI


def main():
    args = handle_args()
    game = GUI(args).init_screen()
    deck = from_csv(args.cards_file)
    deck.set_images(args.cards_front, args.cards_back)
    run = True
    while run:
        game.screen.fill((0, 0, 0))
        deck.update_sprites()
        deck.cards.draw(game.screen)
        run = game.handle_events()
        game.refresh()

    game.quit()


if __name__ == '__main__':
    main()
