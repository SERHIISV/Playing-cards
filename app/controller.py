#!/usr/bin/env python
import sys
sys.path.append("..")

from random import randint

from deck_of_cards.app import cards, hand


class Actions:
    """
    Class Actions is a controller of actions

    Available methods:
        - show_hand()
        - show_deck()
        - choose_card()
        - choose_by_index()
        - determine()
        - random_choose()
        - shuffle_deck()
        - compare()
        - sort_by_rank()
        - sort_by_suit()
        - drop_cards()
    """
    def __init__(self):
        self.deck = cards.Cards()
        self.hand = hand.Hand()

    def actions_list(self):
        """
        Output alist of available actions
        """
        print "========================================"
        print "List of available actions in this app:"
        print "----------------------------------------"
        print " 0 - Show the hand"
        print " 1 - Show the deck"
        print " 2 - Choose a card"
        print " 3 - Choose a card by index"
        print " 4 - Determine of chosen card"
        print " 5 - Randomly choose a card"
        print " 6 - Shuffle the deck"
        print " 7 - Compare your card with another one"
        print " 8 - Show the deck by rank"
        print " 9 - Show the deck by suit"
        print " m - MENU | List of available actions"
        print " + - Take a card to hand"
        print " c - Drop a cards from hand"
        print "----------------------------------------"
        print "FOR CHOOSING OF ACTION INPUT A NUMBER"
        print "----------------------------------------"

    def show_hand(self):
        """
        Showing current cards in hand.
        """
        self.hand.__unicode__()

    def show_deck(self):
        """
        Showing current deck.
        """
        print "****************************************"
        for card in self.deck.deck:
            print " ".join(card)
        print "****************************************"

    def choose_card(self):
        """
        :param suit: suit of card which need to get
        :param rank: rank of card which need to get
        """
        print "****************************************"
        print "Enter enter one of suits that is below"
        print " > s - spades"
        print " > c - clubs"
        print " > h - hearts"
        print " > d - diamonds"
        suit = raw_input('Enter a letter >>> ')
        suit = suit.lower()
        if suit not in 'schd':
            print "!!!!!!! There is no of this suit !!!!!!"
        for item in self.deck.suits:
            if item.startswith(suit):
                suit = item

        print "Enter enter one of these runks => [A, K, Q, J, 2-10]"
        rank = raw_input('Enter a rank >>> ')
        rank = rank.upper()
        if rank not in self.deck.ranks:
            return "!!!!!! There is no of this rank !!!!!!"

        chosen_card = (rank, suit)
        print '>>> Your chosen is %s of %s' % (rank, suit)
        print "****************************************"
        return chosen_card

    def take_cards(self):
        card = self.choose_card()
        print "Do you want take this card in your hand?"
        ans = raw_input('Enter y or n >>> ')
        if ans in 'yY':
            self.hand.add(card)
        return card

    def choose_by_index(self):
        """
        Choosing a card by index
        """
        print "****************************************"
        print "Enter index of card in the deck which you want choose"
        value = raw_input('Enter one of 52 >>> ')
        try:
            index = int(value)
            print " of ".join(self.deck.deck[index-1])
            return self.deck.deck[index-1]
        except ValueError:
            print "That is not a number."
            self.choose_by_index()
        print "****************************************"

    def determine(self):
        """
        Determining current place of card in the deck.
        :param index: determined index of card in hand
        """
        card = self.choose_card()

        index = self.deck.deck.index(card) + 1
        output = " >>> Position of card in your hand - %s" % index

        print "****************************************"
        print output
        print "****************************************"
        return index

    def random_choose(self):
        """
        Randomly choosing of a card
        """
        random_card = self.deck.deck[randint(0, len(self.deck.deck))]
        print "****************************************"
        print " >>> Random card is %s" % " of ".join(random_card)
        print "****************************************"
        return random_card

    def shuffle_deck(self):
        """
        Shuffling a deck.
        """
        self.deck.shuffle(self.deck.deck)
        print "****************************************"
        print ">>> Deck are shuffled <<<"
        print "****************************************"

    def compare(self):
        """
        comparing two cards by waight
        """
        first_card = self.choose_card()
        second_card = self.choose_card()

        first_card_index = self.deck.ranks.index(first_card[0])
        second_card_index = self.deck.ranks.index(second_card[0])

        # Converting name of card from tuple to string | Making readable name of card
        first_card = " of ".join(first_card)
        second_card = " of ".join(second_card)

        if first_card_index > second_card_index:
            result = "%s bigger than %s" % (first_card, second_card)
        elif first_card_index < second_card_index:
            result = "%s smoller than %s" % (first_card, second_card)
        elif first_card_index == second_card_index:
            result = "%s equal to %s" % (second_card, first_card)
        print result
        print "****************************************"
        return result

    def sort_by_rank(self):
        """
        Sorting of cards by rank
        """
        self.deck.rank_sort()
        print "****************************************"
        print ">>> Deck are shorted by rank <<<"
        print "****************************************"

    def sort_by_suit(self):
        """
        Sorting of cards by suit
        """
        self.deck.suit_sort()
        print "****************************************"
        print ">>> Deck are shorted by suit <<<"
        print "****************************************"

    def drop_cards(self):
        """
        Droping all cards from hand
        """
        self.hand.clear()
        print ">>>>>>>>>>> Cards are dropped <<<<<<<<<<"
        print "****************************************"
