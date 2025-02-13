class Card:   # inherits from 'object'
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    @property
    def rank(self):  # getter property
        return self._rank
    
    @rank.setter
    def rank(self, value):  # setter property
        # validate value 
        self._rank = value

    @property
    def suit(self):
        return self._suit
    
    @suit.setter
    def suit(self, value):
        self._suit = value
    
    # used when str(obj)
    def __str__(self):   # like .to_string() in Java
        return f"CARD:{self.rank}-{self.suit}"

    def __repr__(self):
        return f"Card('{self.rank}', '{self.suit}')"

if __name__ == "__main__":
    c = Card("J", "Diamonds")  # self + args
    print(c)  # print(str(c))
    # print(f"{c.get_rank() = }")
    print(f"{c.rank = }")
    print(f"{c.suit = }")
    # c.suit = "Hearts"
    print(f"{c._rank = }") # naughty
    c._rank = "2"   # more naughty
    print(f"{c.rank = }")
    print(repr(c))
    print(f"{c = }")

    x = TypeError("this is a test")
    print(x)
    print(repr(x))


    