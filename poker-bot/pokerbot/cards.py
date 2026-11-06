import random

RANKS = "23456789TJQKA"
SUITS = "cdhs"


def create_deck():
    deck = [
        rank + suit
        for rank in RANKS
        for suit in SUITS
    ]

    random.shuffle(deck)

    return deck


def deal_card(deck):
    return deck.pop()


def deal_hand(deck):
    return [deal_card(deck), deal_card(deck)]


def deal_board(deck, count):
    return [deal_card(deck) for _ in range(count)]