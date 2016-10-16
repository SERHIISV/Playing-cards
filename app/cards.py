#!/usr/bin/env python
import itertools
from random import shuffle

class Cards:
    """
    Deck of cards. Making deck and shuffling of a deck
    """
    def __init__(self):
        """
        :param ranks: list of ranks(indexes) of cards
        :param suits: list of suits of cards
        :param cards: list of cards of deck
        """
        self.ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        self.suits = ['spades', 'hearts', 'clubs', 'diamonds']
        self.deck = list(itertools.product(self.ranks, self.suits))

    def shuffle(self, deck):
        """
        Shuffles cards in the deck randomly
        """
        deck = self.deck
        shuffle(deck)

    def suit_sort(self):
        """
        Sorting of cards by suit
        """
        self.deck = sorted(self.deck, key=lambda card: card[1])

    def rank_sort(self):
        """
        Sorting of cards by rank
        """
        for rank in self.ranks:
            self.deck = sorted(self.deck, key=lambda card: card[0] == rank)
