#!/usr/bin/env python
from app import controller, cards


class Main(object):
    """
    Class Main is controlling of available actions
    """
    def __init__(self):
        self.controller = controller.Actions()
        self.cards = cards.Cards()

    def manage(self):
        """
        Processing of chosen actions
        """
        while True:
            pressed_key = raw_input("Enter a number of action: ")
            if pressed_key == '1':
                main.controller.show_deck()
            elif pressed_key == '2':
                main.controller.choose_card()
            elif pressed_key == '3':
                main.controller.choose_by_index()
            elif pressed_key == '4':
                main.controller.determine()
            elif pressed_key == '5':
                main.controller.random_choose()
            elif pressed_key == '6':
                main.controller.shuffle_deck()
            elif pressed_key == '7':
                main.controller.compare()
            elif pressed_key == '8':
                main.controller.sort_by_rank()
            elif pressed_key == '9':
                main.controller.sort_by_suit()
            elif pressed_key == '0':
                main.controller.show_hand()
            elif pressed_key in 'mM':
                main.controller.actions_list()
            elif pressed_key in '+':
                main.controller.take_cards()
            elif pressed_key in 'cC':
                main.controller.drop_cards()
            elif pressed_key in 'qQ':
                print "---------------Goodbye!!!---------------"
                print "========================================"
                break
            else:
                print "!!!!!! Wrong input value !!!!!!"


print "++++++++++++++++++++++++++++++++++++++++"
print "------------ Hello, World!!! -----------"

if __name__ == "__main__":
    main = Main()
    main.controller.actions_list()
    main.manage()
