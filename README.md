#  Monte Carlo Poker AI

A command-line Texas Hold'em poker game where you play against an AI opponent that uses Monte Carlo simulations to estimate hand equity and make decisions.

The AI evaluates its chances of winning by simulating thousands of possible poker outcomes and uses expected value (EV) and pot odds to decide whether to call, fold, bet, or check.


##  Technologies Used

- Python
- Monte Carlo Simulation
- Poker Hand Evaluation
- Probability and Expected Value (EV)

### Dependencies

- `phevaluator`

## 📁 Project Structure

```text
poker-bot/
│
├── main.py
│
└── pokerbot/
    │
    ├── __init__.py
    ├── ai.py
    ├── cards.py
    ├── game.py
    └── simulator.py
