from .card import Card
from pygame.sprite import Group as SpriteGroup


class Deck:
    def __init__(self):
        self.cards = SpriteGroup()

    def add_card(self, question: str, answer: str):
        """:param question the question for the Card to add to the deck
            :param answer the Card's answer"""
        self.cards.add(Card().set_fields(question, answer))
        return self

    def add_card_from_list(self, add: [str]):
        """:param add list of two strings formatted [question, answer]"""
        self.cards.add(Card().set_fields(add[0], add[1]))
        return self

    def add_card_from_obj(self, add: Card):
        """:param add the Card object to add to this deck"""
        self.cards.add(add)
        return self

    def set_images(self, front: str, back: str):
        """Set the background images for all self.cards
        :param front .jpg (500x250) pixels to use for the front
        :param back .jpg to use for the back"""
        for card in self.cards:
            card.set_imgs(front, back)

    def update_sprites(self):
        for card in self.cards:
            card.update()

    def print(self):
        """Print each question: answer in the deck"""
        for card in self.cards:
            print(f"{card.question}: {card.answer}")
