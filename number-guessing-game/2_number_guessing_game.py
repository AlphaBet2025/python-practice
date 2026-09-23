"""
PROJECT 2: NUMBER GUESSING GAME
================================
WHAT THIS TEACHES:
- The `random` module
- Tracking state across loop iterations (attempts, guesses)
- Giving feedback based on conditionals (too high / too low)
- Basic input validation
"""

import random


def play_round(lower=1, upper=100):
    """Plays one round of the game. Returns the number of attempts taken."""

    # random.randint(a, b) picks a random INTEGER, including both endpoints.
    secret = random.randint(lower, upper)
    attempts = 0

    print(f"\nI'm thinking of a number between {lower} and {upper}.")

    while True:  # loop forever until the player guesses correctly (then we `return`)
        guess_raw = input("Your guess: ").strip()

        # Validate the input is actually a whole number before using it
        if not guess_raw.isdigit():
            print("Please enter a whole number.")
            continue

        guess = int(guess_raw)
        attempts += 1  # we only count it as an attempt once it's a valid guess

        if guess < secret:
            print("Too low!")
        elif guess > secret:
            print("Too high!")
        else:
            # This is the "happy path" -- the guess matches.
            print(f"Correct! You got it in {attempts} attempts.")
            return attempts


def main():
    print("=== Number Guessing Game ===")

    best_score = None  # None means "no rounds played yet"

    while True:
        attempts = play_round()

        # Track a "high score" (fewest attempts) across multiple rounds.
        # This shows how a variable can persist across loop iterations.
        if best_score is None or attempts < best_score:
            best_score = attempts
            print(f"New best score: {best_score} attempts!")
        else:
            print(f"Your best is still {best_score} attempts.")

        again = input("Play again? (y/n): ").strip().lower()
        if again != "y":
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()
