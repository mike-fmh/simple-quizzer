from argparse import ArgumentParser


def handle_args():
    """Create all arguments, and return the parsed given arguments"""
    args = ArgumentParser()
    args.add_argument("--file",
                      help="Path to the file containing questions and answers for your flashcards")

    return args.parse_args()
