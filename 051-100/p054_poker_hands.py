import time
import os
start = time.time()


VALUES = {'2': 2,
          '3': 3,
          '4': 4,
          '5': 5,
          '6': 6,
          '7': 7,
          '8': 8,
          '9': 9,
          'T': 10,
          'J': 11,
          'Q': 12,
          'K': 13,
          'A': 14}

SUITS = {'H': 1,
         'S': 2,
         'D': 3,
         'C': 4}

RANKS = {'HC': 1,       # high card
         'OP': 2,       # one pair
         'TP': 3,       # two pairs
         'TK': 4,       # three of a kind
         'ST': 5,       # straight
         'FL': 6,       # flush
         'FH': 7,       # full house
         'FK': 8,       # four of a kind
         'SF': 9,       # straight flush
         'LF': 10}      # royal straight flush


def high_card(hand):
    pass


def one_pair(hand):
    pass


def two_pairs(hand):
    pass


def three(hand):
    pass


def straight(hand):
    pass


def flush(hand):
    pass


def full_house(hand):
    pass


def four(hand):
    pass


def straight_flush(hand):
    pass


def royal_flush(hand):
    pass


def win(p1, p2):
    pass
    

'''




    High Card: Highest value card.
    One Pair: Two cards of the same value.
    Two Pairs: Two different pairs.
    Three of a Kind: Three cards of the same value.
    Straight: All cards are consecutive values.
    Flush: All cards of the same suit.
    Full House: Three of a kind and a pair.
    Four of a Kind: Four cards of the same value.
    Straight Flush: All cards are consecutive values of same suit.
    Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.

'''
hands_file = f"{os.path.dirname(os.path.realpath(__file__))}/p054_poker.txt"
with open(hands_file, 'rt') as f:
    hands = [line.rstrip('\n') for line in f.readlines()]

p1score = 0
p2score = 0

for hand in hands:
    p1hand = hand.split(" ")[:5]
    p2hand = hand.split(" ")[5:]
    if win(p1hand, p2hand):
        p1score += 1
    else:
        p2score += 1


result = p1score

print(f"Result: {result}")
end = time.time()
print(f"{round((end - start)*1000)} ms")
