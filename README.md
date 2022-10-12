# WIP Learn Temporal PythonSDK
Build a poker game that demonstrates the value of Temporal and helps me get to know the PythonSDK

## AppDev Process
- [x] build out deck
- [x] shuffle
- [x] deal
- [ ] single player game score [in progress]
- [ ] two player game score
- [ ] bet function
- [ ] [foundations](https://docs.temporal.io/application-development/foundations)
- [ ] [features](https://docs.temporal.io/application-development/features)
- [ ] [observability](https://docs.temporal.io/application-development/observability)
- [ ] [testing](https://docs.temporal.io/application-development/testing)
- [ ] [worker performance](https://docs.temporal.io/application-development/worker-performance)

### Classes to Define
- card / value / suit
- deck / shuffle / deal
- score / flush / straight / high card
- player / bot / person
- bet / money transfer / winning / cashing out
- leaderboard
- tx holdem rules / pre-flop / flop / turn / river

### How to Play
~~~
  > deck = StandardDeck()
  > rain = Player()
  > deck.shuffle()
  Deck Shuffled
  > rain.cards.append(deck.deal())
  > rain.cards.append(deck.deal())
  > rain.cards.append(deck.deal())
  > rain.cards.append(deck.deal())
  > rain.cards.append(deck.deal())
  > rain.cards
  [Card, Card, Card, Card, Card]
  > rain.cards[0].showing="True"
  > rain.cards
  [King of Hearts, Card, Card, Card, Card]
  > rain.cards[1].showing="True"
  > rain.cards[2].showing="True"
  > rain.cards[3].showing="True"
  > rain.cards[4].showing="True"
  > rain.cards
  [King of Hearts, Three of Diamonds, King of Clubs, Five of Hearts, Four of Hearts]
  > rain.cards[1] = deck.deal()
  > rain.cards[3] = deck.deal()
  > rain.cards[4] = deck.deal()
  > rain.cards[1].showing="True"
  > rain.cards[3].showing="True"
  > rain.cards[4].showing="True"
  > rain.cards
  [King of Hearts, Queen of Hearts, King of Clubs, Jack of Hearts, Ace of Hearts]
  > score = PokerScorer(rain.cards)
  > score.straight()
  False
  > score.flush()
  False
  > score.highCard()
  Ace of Hearts
~~~
