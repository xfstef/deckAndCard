import random

from constants import SUITS, VALUES, JOKERS
from card import Card


class Deck:
    cards = []

    def __init__(self):
        self.build()

    def build(self):
        self.cards = []
        for suit in SUITS:
            for value in VALUES:
                self.cards.append(Card(suit, value))
        for joker in JOKERS:
            self.cards.append(Card(joker[0], joker[1]))

    def show(self):
        for card in self.cards:
            card.show()

    def shuffle(self):
        for i in range(len(self.cards) - 1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    def draw(self) -> str:
        if len(self.cards) > 0:
            next_card = self.cards.pop()
            return next_card.show()
        else:
            return "No more cards in the deck!"
