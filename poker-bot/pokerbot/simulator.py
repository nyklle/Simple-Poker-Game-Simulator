import random

from phevaluator import evaluate_cards

from pokerbot.cards import create_deck


def monte_carlo_equity(
    ai_hand,
    board,
    simulations=5000
):

    known_cards = ai_hand + board

    if len(ai_hand) != 2:
        raise ValueError("AI must have exactly 2 cards")

    if len(board) > 5:
        raise ValueError("Board cannot exceed 5 cards")

    if len(set(known_cards)) != len(known_cards):
        raise ValueError("Duplicate cards detected")

    deck = create_deck()

    for card in known_cards:

        if card not in deck:
            raise ValueError(f"Invalid card: {card}")

        deck.remove(card)

    wins = 0
    losses = 0
    ties = 0

    for _ in range(simulations):

        cards = random.sample(
            deck,
            2 + (5 - len(board))
        )

        opponent_hand = cards[:2]

        simulated_board = (
            board + cards[2:]
        )

        ai_score = evaluate_cards(
            *(ai_hand + simulated_board)
        )

        opponent_score = evaluate_cards(
            *(opponent_hand + simulated_board)
        )

        if ai_score < opponent_score:
            wins += 1

        elif ai_score > opponent_score:
            losses += 1

        else:
            ties += 1

    equity = (
        wins + ties * 0.5
    ) / simulations

    return {
        "wins": wins,
        "losses": losses,
        "ties": ties,
        "equity": equity
    }