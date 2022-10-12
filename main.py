import random

class Card(object):
  def __init__(self, name, value, suit):
    self.value = value
    self.suit = suit
    self.name = name
    self.showing = False
  def __repr__(self):
    if self.showing:
      return str(self.name) + " of " + self.suit
    else:
      return "Card"

class Deck(object):
  def shuffle(self, times=1):
    random.shuffle(self.cards)
    print("Deck Shuffled")
  
  def deal(self):
    return self.cards.pop(0)

class StandardDeck(object):
  def __init__(self):
    self.cards = []
    suits = ["Hearts", "Spades", "Diamonds", "Clubs"]
    values = {"Two":2, 
              "Three":3, 
              "Four":4, 
              "Five":5, 
              "Six":6, 
              "Seven":7, 
              "Eight":8, 
              "Nine":9, 
              "Ten":10, 
              "Jack":11, 
              "Queen":12, 
              "King":13, 
              "Ace":14}
    for name in values:
      for suit in suits:
        self.cards.append(Card(name, values[name], suit))

  def __repr__(self):
    return "Standard deck of cards:{0} cards remaining".format(len(self.cards))

class Player(object):
  def __init__(self):
    self.cards = []

  def cardCount(self):
    return len(self.cards)

class PokerScorer(object):
  def __init__(self, cards):
    # Number of cards
    if not len(cards) == 5:
      return "Error: Wrong number of cards"

    self.cards = cards

  def flush(self):
    suits = [card.suit for card in self.cards]
    if len(set(suits)) == 1:
      return True
    else:
      return False

  def straight(self):
    values = [card.value for card in self.cards]
    values.sort()

    if not len(set(values)) == 5:
      return False
    if value[4] == 14 and value[3] == 5 and value[2] == 4 and value[1] == 3 and value[0] == 2:
      return True
    else:
      if not value[0] + 1 == value[1]: return False
      if not value[1] + 1 == value[2]: return False
      if not value[2] + 1 == value[3]: return False
      if not value[3] + 1 == value[4]: return False

    return True

  def highCard(self):
    values = [card.value for card in self.cards]
    highCard = None
    for card in self.cards:
      if highCard is None:
        highCard = card
      elif highCard.value < card.value:
        highCard = card
    return highCard
