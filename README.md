# Number Guessing Game 🎯

A simple command-line number guessing game built in Python. The computer
picks a random number, and you try to guess it within a limited number
of attempts based on the difficulty you choose.

## Features
- Three difficulty levels (Easy / Medium / Hard)
- Input validation (rejects non-numeric or out-of-range guesses)
- "Too high" / "too low" hints
- Play again option

## How to Run

```bash
python number_guessing_game.py
```

## Requirements
- Python 3.x (no external libraries needed)

## Example

```
Select a difficulty level:
1. Easy   (1-50,  10 attempts)
2. Medium (1-100, 7 attempts)
3. Hard   (1-200, 5 attempts)
Enter your choice (1/2/3): 2

I'm thinking of a number between 1 and 100.
You have 7 attempts. Good luck!

Enter your guess (1-100): 50
Too low! You have 6 attempt(s) left.
```
