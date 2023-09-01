from deck import Deck
from card import Card
from constants import SUITS, VALUES

class TestDeck:
    def __init__(self):
        test_deck = Deck()

        checkDeckStructure(test_deck)
        checkDraw(test_deck)
        checkDeckRebuild(test_deck)

        print('All tests passed!')


def checkDeckStructure(deck):
    """
    Check if the deck is a list of 54 cards with the correct attributes.
    """
    assert isinstance(deck, Deck)
    assert len(deck.cards) == 54

    for card in deck.cards:
        assert isinstance(card, Card)
        assert isinstance(card.suit, str)
        assert isinstance(card.value, str)
        suit = card.suit
        assert suit in SUITS or suit == 'Joker'
        value = card.value
        assert value in VALUES or value in ('Black', 'Red')


def checkDraw(deck):
    """
    Check if the draw method works correctly.
    """
    assert isinstance(deck, Deck)
    assert len(deck.cards) == 54
    drawn_card = deck.draw()
    words = drawn_card.split()
    assert words[0] in VALUES or words[0] in ('Black', 'Red')
    assert words[1] == 'of'
    assert words[2] in SUITS or words[2] == 'Joker'
    assert len(deck.cards) == 53
    # Test drawing the rest of the cards
    while len(deck.cards) > 0:
        drawn_card = deck.draw()
        words = drawn_card.split()
        assert words[0] in VALUES or words[0] in ('Black', 'Red')
        assert words[1] == 'of'
        assert words[2] in SUITS or words[2] == 'Joker'
    # Test drawing from an empty deck
    assert len(deck.cards) == 0
    assert deck.draw() == "No more cards in the deck!"
    # Rebuild the deck for the next tests
    deck.build()


def checkDeckRebuild(deck):
    """
    Check if the deck rebuilds correctly.
    """
    assert isinstance(deck, Deck)
    assert len(deck.cards) == 54
    deck.draw()
    assert len(deck.cards) == 53
    deck.build()
    assert isinstance(deck, Deck)
    assert len(deck.cards) == 54
