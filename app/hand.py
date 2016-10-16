#!/usr/bin/env python
from deck_of_cards.app import deck


class Hand:
    """
    Class Hand is determine cards which chosen
    """
    def __init__(self):
        self.cards = []

    def __unicode__(self):
        print "****************************************"

        if self.cards:
            for card in self.cards:
                print " of ".join(card)
        else:
            print " No cards in your hand \n For choosing a card enter \"+\""

        print "****************************************"

    def clear(self):
        """
        Delete all cards from hand
        """
        del self.cards[:]

    def add(self, card):
        """
        Add a card to hand
        """
        self.cards.append(card)
        print ">>>>>>> Card %s is added <<<<<<<" % " of ".join(card)
        print "****************************************"
