import flashquiz.flashcards as flash
from flashquiz.parse import from_csv


d = flash.Deck()

d.add_card("hello", "world")
d.print()
print("\n")

d2 = from_csv(r"/Users/michaelfelix/Downloads/testSheet1.csv")
d2.print()



