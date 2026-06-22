🎯 Number Guessing Game
A fun and interactive number guessing game where players try to guess a randomly generated number within a limited number of attempts.
---
📖 Table of Contents
About the Project
Features
Demo
Getting Started
Prerequisites
Installation
How to Play
Game Rules
Project Structure
Technologies Used
Contributing
License
---
📌 About the Project
The Number Guessing Game is a simple yet engaging game where the computer picks a secret number and the player must figure it out using hints like "Too High" or "Too Low." It's a great project for beginners to practice logic, conditionals, and loops.
---
✨ Features
🎲 Randomly generated secret number each round
🔁 Multiple difficulty levels (Easy, Medium, Hard)
💡 Hints after each incorrect guess (Too High / Too Low)
📊 Tracks number of attempts
🏆 Displays win/loss message with attempt count
🔄 Option to restart the game after each round
---
🚀 Demo
```
Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
You have 10 attempts. Good luck!

Enter your guess: 50
Too low! Try again. (Attempts left: 9)

Enter your guess: 75
Too high! Try again. (Attempts left: 8)

Enter your guess: 63
🎉 Correct! You guessed it in 3 attempts!
```
---
🛠️ Getting Started
Prerequisites
Make sure you have the following installed:
Python 3.x (or Node.js / Java depending on your implementation)
Installation
Clone the repository:
```bash
git clone https://github.com/your-username/number-guessing-game.git
```
Navigate into the project directory:
```bash
cd number-guessing-game
```
Run the game:
```bash
python game.py
```
---
🎮 How to Play
Run the game in your terminal or browser.
The computer randomly picks a number within a defined range (e.g., 1–100).
Enter your guess when prompted.
The game tells you if your guess is too high, too low, or correct.
Keep guessing until you find the number or run out of attempts.
After the game ends, choose to play again or exit.
---
📋 Game Rules
Difficulty	Range	Max Attempts
Easy	1–50	15
Medium	1–100	10
Hard	1–200	7
You win if you guess the correct number within the allowed attempts.
You lose if you exhaust all attempts without guessing correctly.
The secret number is revealed if you lose.
---
📁 Project Structure
```
number-guessing-game/
│
├── game.py           # Main game logic
├── utils.py          # Helper functions (input validation, hints, etc.)
├── README.md         # Project documentation
└── requirements.txt  # Dependencies (if any)
```
---
💻 Technologies Used
Language: Python 3.x (update as per your stack)
Concepts: Random number generation, loops, conditionals, user input handling
---
🤝 Contributing
Contributions are welcome! Here's how you can help:
Fork the repository
Create a new branch: `git checkout -b feature/your-feature-name`
Make your changes and commit: `git commit -m "Add your feature"`
Push to your branch: `git push origin feature/your-feature-name`
Open a Pull Request
---
📄 License
This project is licensed under the MIT License.
---
👨‍💻 Author
Your Name
GitHub: @your-username
Email: your.email@example.com
---
> Made with ❤️ and a little bit of luck 🎲
