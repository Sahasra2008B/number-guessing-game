"""
Number Guessing Game
---------------------
The computer picks a random number within a range, and the player
tries to guess it within a limited number of attempts, getting
"too high" / "too low" hints along the way.
"""

import random


def get_difficulty():
    print("\nSelect a difficulty level:")
    print("1. Easy   (1-50,  10 attempts)")
    print("2. Medium (1-100, 7 attempts)")
    print("3. Hard   (1-200, 5 attempts)")

    while True:
        choice = input("Enter your choice (1/2/3): ").strip()
        if choice == "1":
            return 1, 50, 10
        elif choice == "2":
            return 1, 100, 7
        elif choice == "3":
            return 1, 200, 5
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


def get_valid_guess(low, high):
    while True:
        guess_input = input(f"Enter your guess ({low}-{high}): ").strip()
        if not guess_input.lstrip("-").isdigit():
            print("That's not a valid number. Try again.")
            continue

        guess = int(guess_input)
        if guess < low or guess > high:
            print(f"Please enter a number between {low} and {high}.")
            continue

        return guess


def play_round():
    low, high, max_attempts = get_difficulty()
    secret_number = random.randint(low, high)
    attempts_used = 0

    print(f"\nI'm thinking of a number between {low} and {high}.")
    print(f"You have {max_attempts} attempts. Good luck!\n")

    while attempts_used < max_attempts:
        guess = get_valid_guess(low, high)
        attempts_used += 1

        if guess == secret_number:
            print(f"\n🎉 Correct! You guessed it in {attempts_used} attempt(s).")
            return True

        remaining = max_attempts - attempts_used
        if guess < secret_number:
            print("Too low!", end=" ")
        else:
            print("Too high!", end=" ")

        if remaining > 0:
            print(f"You have {remaining} attempt(s) left.\n")
        else:
            print()

    print(f"\n😢 Out of attempts! The number was {secret_number}.")
    return False


def main():
    print("=" * 40)
    print("       WELCOME TO THE NUMBER GUESSING GAME")
    print("=" * 40)

    wins = 0
    rounds = 0

    while True:
        play_round()
        rounds += 1

        again = input("\nPlay again? (y/n): ").strip().lower()
        if again != "y":
            break

    print("\nThanks for playing! Goodbye 👋")


if __name__ == "__main__":
    main()
