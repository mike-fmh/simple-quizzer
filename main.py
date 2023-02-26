import flashquiz.flashcards as flash
from flashquiz.flashcards.parser import from_csv
from flashquiz.quizzer import main

d = flash.Deck()

d.add_card("hello", "world")
d.print()
print("\n")

d2 = from_csv(r"/Users/michaelfelix/Downloads/testSheet1.csv")
d2.print()

main()
