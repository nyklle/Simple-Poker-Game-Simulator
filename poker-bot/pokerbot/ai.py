from pokerbot.simulator import monte_carlo_equity


def calculate_ev(equity, pot, call_amount):

    return (
        equity * pot
        - (1 - equity) * call_amount
    )


def calculate_pot_odds(pot, call_amount):

    if pot + call_amount <= 0:
        return 0

    return call_amount / (pot + call_amount)


def ai_decision(
    ai_hand,
    board,
    pot,
    call_amount=0,
    simulations=5000
):

    result = monte_carlo_equity(
        ai_hand,
        board,
        simulations
    )

    equity = result["equity"]

    print("\n[AI ANALYSIS]")

    print(f"Estimated equity: {equity:.2%}")

    print(f"Simulations: {simulations}")

    if call_amount > 0:

        pot_odds = calculate_pot_odds(
            pot,
            call_amount
        )

        ev = calculate_ev(
            equity,
            pot,
            call_amount
        )

        print(f"Pot odds: {pot_odds:.2%}")

        print(f"Expected value: ${ev:.2f}")

        if ev > 0:

            print("[AI ACTION] CALL")

            return "call"

        else:

            print("[AI ACTION] FOLD")

            return "fold"

    else:

        if equity >= 0.65:

            print("[AI ACTION] BET")

            return "bet"

        else:

            print("[AI ACTION] CHECK")

            return "check"