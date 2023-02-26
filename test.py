import flashquiz.flashcards as flash
from flashquiz.flashcards.parser import from_csv
from flashquiz.quizzer import main

d = flash.Deck()

d.add_card("hello", "world")
d.print()
print("\n")


main()

while True:
    pass
