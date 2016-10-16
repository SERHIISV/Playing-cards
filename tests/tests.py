import sys
sys.path.append("..")

import unittest

from mock import patch

import data_for_tests as data

#from . import Main
from deck_of_cards.app import hand
from deck_of_cards.app import cards
from deck_of_cards.app import controller


class TestMethods(unittest.TestCase):
    def setUp(self):
        self.act = controller.Actions()
        self.cards = cards.Cards()
        self.hand = hand.Hand()
        #self.main = Main()

    @patch('__builtin__.raw_input')
    def test_choose_by_index(self, m_input):
        print ">>>>>>>>>> test_choose_by_index"
        m_input.side_effect = ['1']
        self.assertEqual(self.act.choose_by_index(), ('2', 'spades'))

    @patch('__builtin__.raw_input')
    def test_choose_card(self, m_input):
        print ">>>>>>>>>> test_choose_card"
        m_input.side_effect = ['s', 'a', 'y']
        self.assertEqual(self.act.choose_card(), ('A', 'spades'))

    @patch('__builtin__.raw_input')
    def test_determine(self, m_input):
        print ">>>>>>>>>> test_determine"
        m_input.side_effect = ['s', '2', 'y']
        self.assertEqual(self.act.determine(), 1)

    def test_random_choose(self):
        print ">>>>>>>>>> test_random_choose"
        first = self.act.random_choose()
        second = self.act.random_choose()
        assert first != second

    @patch('__builtin__.raw_input')
    def test_compare(self, m_input):
        print ">>>>>>>>>> test_compare"
        m_input.side_effect = ['s', '2', 's', 'a']
        self.assertEqual(self.act.compare(), '2 of spades smoller than A of spades')

    def test_shuffle_deck(self):
        print ">>>>>>>>>> test_shuffle_deck"
        self.cards.shuffle(data.deck)
        assert self.cards.deck != data.deck

    def test_sort_by_suit(self):
        print ">>>>>>>>>> test_sort_by_suit"
        self.cards.suit_sort()
        for card, true_card in zip(self.cards.deck, data.deck_by_suit):
            self.assertEqual(card[1], true_card[1])

    def test_sort_by_rank(self):
        print ">>>>>>>>>> test_sort_by_rank"
        self.cards.rank_sort()
        for card, true_card in zip(self.cards.deck, data.deck):
            self.assertEqual(card[0], true_card[0])

if __name__ == '__main__':
    log_file = 'tests/log_file.txt'
    f = open(log_file, "w")
    suite = unittest.TestLoader().loadTestsFromTestCase(TestMethods)
    unittest.TextTestRunner(f, verbosity=2).run(suite)
    log_file = 'log_file.txt'
    f.close()
