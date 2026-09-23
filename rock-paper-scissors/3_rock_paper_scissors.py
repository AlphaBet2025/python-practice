"""
PROJECT 3: ROCK PAPER SCISSORS
===============================
WHAT THIS TEACHES:
- Encoding "rules" as data (a dictionary) instead of hardcoded if/elif logic
- random.choice() for picking from a list
- Keeping a running score with a dictionary
- Writing a clean win/lose/tie check in very few lines
"""

import random

CHOICES = ["rock", "paper", "scissors"]

# BEATS[x] tells you what `x` beats. e.g. rock beats scissors.
# Encoding rules as data like this means adding "lizard/spock" later
# would just mean editing this dictionary, not rewriting your logic.
BEATS = {
    "rock": "scissors",
    "paper": "rock",
    "scissors": "paper",
}


def get_player_choice():
    while True:
        choice = input(f"Choose {CHOICES}: ").strip().lower()
        if choice in CHOICES:
            return choice
        print("Invalid choice, try again.")


def decide_winner(player, computer):
    """Returns 'player', 'computer', or 'tie'."""
    if player == computer:
        return "tie"
    # BEATS[player] gives what `player` beats. If that equals the
    # computer's choice, the player wins.
    if BEATS[player] == computer:
        return "player"
    return "computer"


def main():
    print("=== Rock Paper Scissors ===  (Ctrl+C or 'q' to quit)\n")

    # A dictionary is a clean way to keep multiple related counters together
    scores = {"player": 0, "computer": 0, "tie": 0}

    while True:
        player = input(f"Choose {CHOICES} or 'q' to quit: ").strip().lower()
        if player == "q":
            break
        if player not in CHOICES:
            print("Invalid choice, try again.\n")
            continue

        computer = random.choice(CHOICES)
        result = decide_winner(player, computer)
        scores[result] += 1

        print(f"You chose {player}, computer chose {computer}.")
        if result == "tie":
            print("It's a tie!")
        else:
            print(f"{result.capitalize()} wins this round!")

        print(f"Score -> You: {scores['player']} | Computer: {scores['computer']} | Ties: {scores['tie']}\n")

    print("\nFinal score:", scores)


if __name__ == "__main__":
    main()
