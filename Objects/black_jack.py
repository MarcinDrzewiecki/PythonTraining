__author__ = 'drzewko'

class Card(object):
    RANKS = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
    SUITS = ["C","D","H","S"]

    def __init__(self,suit,rank):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        rep = self.rank + self.suit
        return rep

class Hand(object):

    def __init__(self):
        self.cards = []

    def __str__(self):
        if self.cards:
            rep = ""
            for card in self.cards:
                rep += str(card) + " "
        else:
            rep = "<pusta>"
        return rep

    def add(self,card):
        self.cards.append(card)

    def clear(self):
        self.cards=[]

    def give(self,card,other_hand):
        self.cards.remove(card)
        other_hand.add(card)


class Deck(Hand):

    def populate(self):
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self.add(Card(suit,rank))

    def shuffle(self):
        import random
        random.shuffle(self.cards)

    def deal(self,hands,num_of_cards=1):
        for round in range(num_of_cards):
            for hand in hands:
                if self.cards:
                    top_card=self.cards[0]
                    self.give(top_card,hand)
                else:
                    print("No more cards")

deck = Deck()

deck.populate()
deck.shuffle()
my_hand = Hand()
your_hand = Hand()
hands = [my_hand,your_hand]
deck.deal(hands,5)
print (deck)
print (my_hand)