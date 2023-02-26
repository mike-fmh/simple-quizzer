from argparse import ArgumentParser
from .gui.constants import Screen


def handle_args():
    """Create all arguments, and return the parsed given arguments"""
    args = ArgumentParser()
    args.add_argument("--file",
                      help="Path to the file containing questions and answers for your flashcards")
    args.add_argument("--title",
                      type=str,
                      help="Window title",
                      default="FlashQuiz")
    args.add_argument("--h",
                      type=int,
                      help="Window height",
                      default=Screen.height)
    args.add_argument("--w",
                      type=int,
                      help="Window width",
                      default=Screen.width)

    return args.parse_args()
