import pygame
from .flashcards.parser import from_csv
from .args import handle_args
from .gui import GUI


def main():
    args = handle_args()
    GUI(args).init_screen()
