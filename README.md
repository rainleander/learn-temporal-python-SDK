# WIP Learn Temporal PythonSDK
Build a poker game that demonstrates the value of Temporal and helps me get to know the PythonSDK

## AppDev Process
- [x] deck
- [x] shuffle
- [x] deal
- [x] score
- [x] single player game 
- [x] [workflow](https://docs.temporal.io/application-development/foundations) 
- [x] [activities](https://docs.temporal.io/application-development/features) 
- [ ] write blog post (in progress)
- [ ] [signals](https://docs.temporal.io/concepts/what-is-a-signal/)
- [ ] [queries](https://docs.temporal.io/concepts/what-is-a-query/)
- [ ] upgrade: two player game score
- [ ] upgrade: bet function

### Feature Requests Roadmap
- player / bot / person
- bet / money transfer / winning / cashing out
- leaderboard
- tx holdem rules / pre-flop / flop / turn / river

### How to Play
~~~
> python3 main.py
You have 100 points

Deck Shuffled
[10♠, J♡, 4♡, A♣, K♢]
Which cards do you want to discard? ( ie. 1, 2, 3 )
*Just hit return to hold all, type exit to quit
3
[10♠, J♡, 3♣, A♣, K♢]

You have 95 points

Deck Shuffled
[A♡, 8♣, Q♣, 5♡, 3♣]
Which cards do you want to discard? ( ie. 1, 2, 3 )
*Just hit return to hold all, type exit to quit
2, 3, 4, 5
[A♡, A♢, 10♡, 10♠, J♠]
Two Pairs!
+10

You have 100 points

Deck Shuffled
[3♠, 10♢, 6♡, 4♠, 8♡]
Which cards do you want to discard? ( ie. 1, 2, 3 )
*Just hit return to hold all, type exit to quit
exit
~~~
