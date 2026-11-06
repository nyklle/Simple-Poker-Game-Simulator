from phevaluator import evaluate_cards

from pokerbot.cards import (
    create_deck,
    deal_hand,
    deal_board
)

from pokerbot.ai import ai_decision


STARTING_STACK = 1000
ANTE = 10


def play_hand():

    deck = create_deck()

    player_hand = deal_hand(deck)

    ai_hand = deal_hand(deck)

    board = []

    player_stack = STARTING_STACK - ANTE

    ai_stack = STARTING_STACK - ANTE

    pot = ANTE * 2

    print("\n==============================")
    print("       TEXAS HOLD'EM")
    print("==============================")

    print(f"\nYour cards: {player_hand}")

    print("AI cards: [HIDDEN]")

    print(f"Starting pot: ${pot}")

    streets = [
        ("FLOP", 3),
        ("TURN", 1),
        ("RIVER", 1)
    ]

    for street, count in streets:

        board.extend(
            deal_board(deck, count)
        )

        print("\n------------------------------")

        print(f"{street}: {board}")

        print("------------------------------")

        print(f"Your stack: ${player_stack}")

        print(f"AI stack: ${ai_stack}")

        print(f"Pot: ${pot}")


        if player_stack > 0:

            while True:

                action = input(
                    "\nYour action (check/bet/fold): "
                ).lower().strip()

                if action in ["check", "bet", "fold"]:
                    break

                print("Invalid action.")

        else:

            action = "check"

        if action == "fold":

            print("\nYou folded!")

            ai_stack += pot

            break


        if action == "bet":

            max_bet = min(
                player_stack,
                ai_stack
            )

            try:
                amount = int(
                    input("Bet amount: $")
                )
            except ValueError:
                print("Invalid amount.")
                return

            if amount <= 0 or amount > max_bet:

                print("Invalid bet amount.")

                return

            player_stack -= amount

            pot += amount


            ai_action = ai_decision(
                ai_hand,
                board,
                pot,
                call_amount=amount,
                simulations=5000
            )

            if ai_action == "fold":

                print("\nAI folds!")

                player_stack += pot

                break

            elif ai_action == "call":

                ai_stack -= amount

                pot += amount

                print(f"AI calls ${amount}")


        elif action == "check":

            print("\nYou check.")

            ai_action = ai_decision(
                ai_hand,
                board,
                pot,
                simulations=5000
            )

            if ai_action == "bet":

                amount = min(
                    max(1, pot // 2),
                    ai_stack,
                    player_stack
                )

                ai_stack -= amount

                pot += amount

                print(f"\nAI bets ${amount}")

                response = input(
                    "Your response (call/fold): "
                ).lower().strip()

                while response not in ["call", "fold"]:

                    response = input(
                        "Enter call or fold: "
                    ).lower().strip()

                if response == "fold":

                    print("\nYou folded!")

                    ai_stack += pot

                    break

                else:

                    player_stack -= amount

                    pot += amount

                    print("You call.")

            else:

                print("AI checks.")

        print("\nBetting round completed.")

    else:


        print("\n==============================")

        print("          SHOWDOWN")

        print("==============================")

        print(f"Your cards: {player_hand}")

        print(f"AI cards: {ai_hand}")

        print(f"Board: {board}")

        player_score = evaluate_cards(
            *(player_hand + board)
        )

        ai_score = evaluate_cards(
            *(ai_hand + board)
        )

        if player_score < ai_score:

            print("\nYOU WIN!")

            player_stack += pot

        elif ai_score < player_score:

            print("\nAI WINS!")

            ai_stack += pot

        else:

            print("\nIT'S A TIE!")

            player_stack += pot // 2

            ai_stack += pot - pot // 2

    print("\n==============================")

    print("         FINAL STACKS")

    print("==============================")

    print(f"Player: ${player_stack}")

    print(f"AI: ${ai_stack}")

    print("==============================")