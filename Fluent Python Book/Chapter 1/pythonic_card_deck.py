import collections
from random import choice

Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self.cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self.cards)

    def __getitem__(self, position):
        return self.cards[position]


beer_card = Card('7', 'diamonds')

deck = FrenchDeck()
len(deck)  # number of cards in the deck
deck[15]  # item at location 15
choice(deck)  # random card from deck
deck[:3]  # look at the top 3 cards
Card('Q', 'hearts') in deck  # check if a specific item exists


# Sorting the deck
suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)


def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]


for card in sorted(deck, key=spades_high):
    print(card)


# Special Methods








