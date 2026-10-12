# Final Project: Personal Mini-Toolkit

## What it does
A menu-driven Python program with three tools: a number guessing game, a to-do list, and a simple calculator. The menu returns after every tool until the user chooses Quit, and an invalid choice gets a polite message instead of a crash.

## How to run it
1. Install Python 3.
2. Open a terminal in this folder.
3. Run: `python toolkit.py`
4. Type a number from 1 to 4 to choose an option.

## Reflection
The hardest part was fitting a menu inside a menu for the to-do list, because I had to keep track of which prompt the program was waiting on. The bug that took longest was typing to-do commands like `add` at the main menu, where they are not valid. I learned that each prompt expects its own kind of input, and that the polite error messages made this easy to spot. I also learned that creating the `tasks` list before the main loop lets it keep its items between tools. With one more week I would save the to-do list to a file so it is still there the next time the program runs, and add a rock-paper-scissors game.