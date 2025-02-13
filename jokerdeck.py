from card import Card
from carddeck import CardDeck

class GameMixin:
    def boop(self):
        print("boop boop")

class JokerDeck(GameMixin, CardDeck):
    def _make_deck(self):
        CardDeck._make_deck(self) # call ancestor version
        for i in 1, 2:
            card = Card(f"JOKER{i}", "JOKER")
            self._cards.append(card)

if __name__ == "__main__":
    j = JokerDeck()
    j.shuffle()
    print(j.cards)
    print(j)
    j.boop()
    print(f"{JokerDeck.mro() = }")
    
