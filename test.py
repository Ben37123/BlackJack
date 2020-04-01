from card import Card

def name_and_suit_test():
    card1 = Card('seven', 'spades',  7, 7, True)
    print(card1)

def color_to_suit_test():
    card1 = Card('seven', 'hearts', 7, 7, True)
    print(card1)

def flip_test():
    card1 = Card('seven', 'hearts', 7, 7, False)
    print(card1)
    card1.flip()
    print(card1)

name_and_suit_test()
color_to_suit_test()
flip_test()