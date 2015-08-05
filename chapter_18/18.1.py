'''		cards		  '''

import random
class Cards(object):
    def __init__(self,suit,rank):
	self.suit=suit
	self.rank=rank
    suit_names=['club','daimond','hearts','spades']
    rank_names=['None','Ace','2','3','4','5','6','7','8','9','10','jack','queen','king']
    def __str__(self):
	return "%s of %s" % (Cards.rank_names[self.rank],Cards.suit_names[self.suit])
    def __cmp__(self,other):
	c1=self.suit,self.rank
	c2=other.suit,other.rank
	return cmp(c1,c2)
	
class Deck(object):
    def __init__(self):
	self.cards=[]
	for suit in range(4):
	    for rank in range(1,14):
		card=Cards(suit,rank)
		self.cards.append(card)
    def __str__(self):
	res=[]
	for card in self.cards:
	    res.append(str(card))
	return '\n'.join(res)
    def shuffle(self):
	random.shuffle(self.cards)
	return self
    def sort(self):
	self.cards.sort(cmp=Cards.__cmp__)
	return self
    def add_card(self,card):
	self.cards.append(card)
	return self
    def pop_card(self):
	self.cards.pop()
	return self
    def move_cards(self,hand,num):
       # hand=Hand('new')
        for i in range(num):
            hand.add_card(self.pop_card())
            return hand
	#exercise_18.3 on think python 
    def deal_hands(self,no_of_hands,cards_per_hand):
	for i in range(no_of_hands):
	    i='hand_num'+str(i)
	    print "the hand is",i
	hand=Hand('new')
	for j in range(cards_per_hand):
	    hand.add_card(self.pop_card())
	    return hand

class Hand(Deck):
    def __init__(self,label=''):
	self.cards=[]
	self.label=label
hand=Hand('new')
deck=Deck()
for x in xrange(13):
    deck.shuffle()

print deck.deal_hands(5,9)
print hand.cards
print hand.label

