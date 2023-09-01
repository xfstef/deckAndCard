

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def show(self):
        print(f"{self.value} of {self.suit}")