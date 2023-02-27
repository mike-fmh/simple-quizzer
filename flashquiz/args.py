from argparse import ArgumentParser
from .gui.constants import Screen


def handle_args():
    """Create all arguments, and return the parsed given arguments"""
    args = ArgumentParser()
    args.add_argument("--file",
                      metavar="INPUT_FILE",
                      help="Path to the file containing questions and answers for your flashcards",
                      default="default.csv")
    args.add_argument("--h",
                      type=int,
                      metavar="WIN_HEIGHT",
                      help="Window height",
                      default=Screen.height)
    args.add_argument("--w",
                      type=int,
                      metavar="WIN_WIDTH",
                      help="Window width",
                      default=Screen.width)
    args.add_argument("--title",
                      type=str,
                      metavar="WIN_TITLE",
                      help="Window title",
                      default=Screen.title)

    return args.parse_args()
