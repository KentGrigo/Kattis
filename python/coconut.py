from enum import Enum

class Hand:
    def __init__(self, playerNumber, state):
        self.playerNumber = playerNumber
        self.state = state

State = Enum('State', 'full split spilled')


numberOfSyllables, numberOfPlayers = list(map(int, input().split()))

hands = []
for playerNumber in range(1, numberOfPlayers + 1):
    hand = Hand(playerNumber, State.full)
    hands.append(hand)

handIndex = 0
while 1 < len(hands):
    handIndex = (handIndex + numberOfSyllables - 1) % len(hands)
    hand = hands[handIndex]
    if hand.state == State.full:
        del hands[handIndex]
        hands.insert(handIndex, Hand(hand.playerNumber, State.split))
        hands.insert(handIndex, Hand(hand.playerNumber, State.split))
    elif hand.state == State.split:
        hand.state = State.spilled
        handIndex = (handIndex + 1) % len(hands)
    elif hand.state == State.spilled:
        del hands[handIndex]

winner = hands[0].playerNumber
print(winner)
