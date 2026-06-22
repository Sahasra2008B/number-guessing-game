"""
Number Guessing Game - GUI Version
------------------------------------
A graphical version of the number guessing game built with Tkinter
(Python's built-in GUI library - no extra installs needed).
"""

import tkinter as tk
from tkinter import messagebox
import random


class NumberGuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Guessing Game")
        self.root.geometry("420x420")
        self.root.resizable(False, False)
        self.root.configure(bg="#1e1e2f")

        self.secret_number = None
        self.low = None
        self.high = None
        self.max_attempts = None
        self.attempts_used = 0

        self.build_difficulty_screen()

    # ---------- Screen builders ----------

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def build_difficulty_screen(self):
        self.clear_screen()

        tk.Label(
            self.root, text="🎯 Number Guessing Game",
            font=("Segoe UI", 18, "bold"), bg="#1e1e2f", fg="#ffffff"
        ).pack(pady=(30, 10))

        tk.Label(
            self.root, text="Choose a difficulty:",
            font=("Segoe UI", 12), bg="#1e1e2f", fg="#cccccc"
        ).pack(pady=(0, 20))

        difficulties = [
            ("Easy (1-50, 10 attempts)", 1, 50, 10),
            ("Medium (1-100, 7 attempts)", 1, 100, 7),
            ("Hard (1-200, 5 attempts)", 1, 200, 5),
        ]

        for label, low, high, attempts in difficulties:
            tk.Button(
                self.root, text=label, width=28, height=2,
                font=("Segoe UI", 10), bg="#3a3a5c", fg="white",
                activebackground="#56568f", relief="flat",
                command=lambda l=low, h=high, a=attempts: self.start_game(l, h, a)
            ).pack(pady=6)

    def start_game(self, low, high, attempts):
        self.low = low
        self.high = high
        self.max_attempts = attempts
        self.attempts_used = 0
        self.secret_number = random.randint(low, high)
        self.build_game_screen()

    def build_game_screen(self):
        self.clear_screen()

        tk.Label(
            self.root,
            text=f"Guess a number between {self.low} and {self.high}",
            font=("Segoe UI", 13, "bold"), bg="#1e1e2f", fg="#ffffff",
            wraplength=380, justify="center"
        ).pack(pady=(30, 5))

        self.attempts_label = tk.Label(
            self.root,
            text=f"Attempts left: {self.max_attempts - self.attempts_used}",
            font=("Segoe UI", 11), bg="#1e1e2f", fg="#aaaaaa"
        )
        self.attempts_label.pack(pady=(0, 15))

        self.guess_entry = tk.Entry(
            self.root, font=("Segoe UI", 14), justify="center", width=10
        )
        self.guess_entry.pack(pady=5)
        self.guess_entry.focus()
        self.guess_entry.bind("<Return>", lambda event: self.check_guess())

        tk.Button(
            self.root, text="Guess", width=14, height=1,
            font=("Segoe UI", 11), bg="#4caf50", fg="white",
            relief="flat", command=self.check_guess
        ).pack(pady=10)

        self.feedback_label = tk.Label(
            self.root, text="", font=("Segoe UI", 12, "bold"),
            bg="#1e1e2f", fg="#ffd54f", wraplength=380, justify="center"
        )
        self.feedback_label.pack(pady=15)

        tk.Button(
            self.root, text="⬅ Back to menu", font=("Segoe UI", 9),
            bg="#1e1e2f", fg="#888888", relief="flat", bd=0,
            command=self.build_difficulty_screen
        ).pack(side="bottom", pady=10)

    def build_result_screen(self, won):
        self.clear_screen()

        if won:
            title = "🎉 You Won!"
            color = "#4caf50"
            message = f"You guessed it in {self.attempts_used} attempt(s)."
        else:
            title = "😢 Out of Attempts"
            color = "#e57373"
            message = f"The number was {self.secret_number}."

        tk.Label(
            self.root, text=title, font=("Segoe UI", 20, "bold"),
            bg="#1e1e2f", fg=color
        ).pack(pady=(60, 15))

        tk.Label(
            self.root, text=message, font=("Segoe UI", 13),
            bg="#1e1e2f", fg="#ffffff"
        ).pack(pady=(0, 30))

        tk.Button(
            self.root, text="Play Again", width=18, height=2,
            font=("Segoe UI", 11), bg="#3a3a5c", fg="white",
            relief="flat", command=self.build_difficulty_screen
        ).pack(pady=5)

        tk.Button(
            self.root, text="Quit", width=18, height=2,
            font=("Segoe UI", 11), bg="#5c3a3a", fg="white",
            relief="flat", command=self.root.destroy
        ).pack(pady=5)

    # ---------- Game logic ----------

    def check_guess(self):
        guess_text = self.guess_entry.get().strip()

        if not guess_text.lstrip("-").isdigit():
            self.feedback_label.config(text="Please enter a valid number.")
            return

        guess = int(guess_text)

        if guess < self.low or guess > self.high:
            self.feedback_label.config(
                text=f"Enter a number between {self.low} and {self.high}."
            )
            return

        self.attempts_used += 1
        self.guess_entry.delete(0, tk.END)

        if guess == self.secret_number:
            self.build_result_screen(won=True)
            return

        remaining = self.max_attempts - self.attempts_used

        if remaining <= 0:
            self.build_result_screen(won=False)
            return

        hint = "Too low!" if guess < self.secret_number else "Too high!"
        self.feedback_label.config(text=hint)
        self.attempts_label.config(text=f"Attempts left: {remaining}")


def main():
    root = tk.Tk()
    NumberGuessingGame(root)
    root.mainloop()


if __name__ == "__main__":
    main()
