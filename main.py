import random

import asyncio
import logging
from dataclasses import dataclass

from temporalio import activity, workflow
from temporalio.client import Client
from temporalio.worker import Worker

@dataclass
class Card(object):
  def __init__(self, name, value, suit, symbol):
    self.value = value
    self.suit = suit
    self.name = name
    self.symbol = symbol

@activity.defn
async def DeckWorkflow(object) -> object:
  def shuffle(self, times=1):
    activity.logger.info("Running activity with parameter %s" % object)
    random.shuffle(self.cards)
    print("Deck Shuffled")

  def deal(self):
    return self.cards.pop(0)

class StandardDeck():
  def __init__(self):
    self.cards = []
    suits = {"Hearts":"♡", "Spades":"♠", "Diamonds":"♢", "Clubs":"♣"}
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
              "Ace":14 }

    for name in values:
      for suit in suits:
        symbolIcon = suits[suit]
        if values[name] < 11:
          symbol = str(values[name])+symbolIcon
        else:
          symbol = name[0]+symbolIcon
        self.cards.append( Card(name, values[name], suit, symbol) )

  def __repr__(self):
    return "Standard deck of cards:{0} remaining".format(len(self.cards))

class Player(object):
  def __init__(self):
    self.cards = []

  def cardCount(self):
    return len(self.cards)

  def addCard(self, card):
    self.cards.append(card)


class PokerScorer(object):
  def __init__(self, cards):
    # Number of cards
    if not len(cards) == 5:
      return "Error: Wrong number of cards"

    self.cards = cards

  def flush(self):
    suits = [card.suit for card in self.cards]
    if len( set(suits) ) == 1:
      return True
    return False

  def straight(self):
    values = [card.value for card in self.cards]
    values.sort()

    if not len( set(values)) == 5:
      return False 

    if values[4] == 14 and values[0] == 2 and values[1] == 3 and values[2] == 4 and values[3] == 5:
      return 5

    else:
      if not values[0] + 1 == values[1]: return False 
      if not values[1] + 1 == values[2]: return False
      if not values[2] + 1 == values[3]: return False
      if not values[3] + 1 == values[4]: return False

    return values[4]

  def highCard(self):
    values = [card.value for card in self.cards]
    highCard = None
    for card in self.cards:
      if highCard is None:
        highCard = card
      elif highCard.value < card.value: 
        highCard=card

    return highCard

  def highestCount(self):
    count = 0
    values = [card.value for card in self.cards]
    for value in values:
      if values.count(value) > count:
        count = values.count(value)

    return count

  def pairs(self):
    pairs = []
    values = [card.value for card in self.cards]
    for value in values:
      if values.count(value) == 2 and value not in pairs:
        pairs.append(value)

    return pairs
        
  def fourKind(self):
    values = [card.value for card in self.cards]
    for value in values:
      if values.count(value) == 4:
        return True

  def fullHouse(self):
    two = False
    three = False
    
    values = [card.value for card in self.cards]
    if values.count(values) == 2:
      two = True
    elif values.count(values) == 3:
      three = True

    if two and three:
      return True

    return False

@workflow.defn
class Poker():
  # start client
  client = await Client.connect("localhost:7233")
  
  # run a worker for the workflow
  async with Worker(
    client,
    task_queue="deck-task-queue",
    workflows=[DeckWorkflow],
  ):

    player = Player()

    # Intial Amount
    points = 100

    # Cost per hand
    handCost = 5

    end = False
    while not end:
      print( "You have {0} points".format(points) )
      print()

      points-=5

      # Hand Loop
      deck = StandardDeck()
      deck.shuffle()

      # Deal Out
      for i in range(5):
        player.addCard(deck.deal())

      validInput = False
      while not validInput:
        print("Which cards do you want to discard? ( ie. 1, 2, 3 )")
        print("*Just hit return to hold all, type exit to quit")
        inputStr = input()

        if inputStr == "exit":
          end=True
          break

        try:
          inputList = [int(inp.strip()) for inp in inputStr.split(",") if inp]

          for inp in inputList:
            if inp > 6:
              continue 
            if inp < 1:
              continue 

          for inp in inputList:
            player.cards[inp-1] = deck.deal()
            player.cards[inp-1].showing = True
 
          validInput = True
        except:
          print("Input Error: use commas to separated the cards you want to hold")

      print(player.cards)
      # Score
      score = PokerScorer(player.cards)
      straight = score.straight()
      flush = score.flush()
      highestCount = score.highestCount()
      pairs = score.pairs()
  
      # Royal flush
      if straight and flush == 14:
        print("Royal Flush!!!")
        print("+2000")
        points += 2000

      # Straight flush
      elif straight and flush != 14:
        print("Straight Flush!")
        print("+250")
        points += 250

      # 4 of a kind
      elif score.fourKind():
        print("Four of a kind!")
        print("+125")
        points += 125

      # Full House
      elif score.fullHouse():
        print("Full House!")
        print("+40")
        points += 40

      # Flush
      elif flush:
        print("Flush!")
        print("+25")
        points += 25
 
      # Straight
      elif straight:
        print("Straight!")
        print("+20")
        points += 20

      # 3 of a kind
      elif highestCount == 3:
        print("Three of a Kind!")
        print("+15")
        points += 15
 
      # 2 pair
      elif len(pairs) == 2:
        print("Two Pairs!")
        print("+10")
        points += 10

      # Jacks or better
      elif pairs and pairs[0] > 10:
        print ("Jacks or Better!")
        print("+5")
        points += 5
 
      player.cards=[]

      print()
      print()
      print()

Poker()
