from pokerbot.game import play_hand


def main():

    print("""
===================================
       MONTE CARLO POKER AI
===================================

Welcome to Texas Hold'em!

You will play against an AI
that calculates equity using
Monte Carlo simulations.

Starting stack: $1000

===================================
""")

    while True:

        play_hand()

        again = input(
            "\nPlay another hand? (y/n): "
        ).lower().strip()

        if again != "y":

            print("\nThanks for playing!")

            break


if __name__ == "__main__":

    main()