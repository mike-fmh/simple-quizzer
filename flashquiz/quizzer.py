import pygame
from .flashcards.parser import from_csv
from .args import handle_args
from .gui import Screen


def main():
    args = handle_args()
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode(Screen.dimensions)
    pygame.display.set_caption("FlashQuiz")
