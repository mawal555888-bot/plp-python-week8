import random

print("Welcome to your Personal Mini-Toolkit!")

tasks = []

while True:
    print()
    print("=== Personal Mini-Toolkit ===")
    print("1. Number Guessing Game")
    print("2. To-Do List")
    print("3. Simple Calculator")
    print("4. Quit")
    choice = input("Choose an option (1-4): ")

    if choice == "1":
        # Number Guessing Game: the user guesses a secret number from 1 to 20
        # and gets a hint (too low or too high) after each guess.
        secret = random.randint(1, 20)
        guess = 0
        tries = 0
        print("I am thinking of a number from 1 to 20.")
        while guess != secret:
            text = input("Your guess: ")
            try:
                guess = int(text)
            except ValueError:
                print("Please type a whole number.")
                continue
            tries = tries + 1
            if guess < secret:
                print("Too low! Try again.")
            elif guess > secret:
                print("Too high! Try again.")
            else:
                print(f"Correct! You found it in {tries} tries.")
    elif choice == "2":
        # To-Do List: add, show and remove tasks from a list that changes
        # while the program runs.
        while True:
            action = input("To-Do List: add / show / remove / back: ")
            if action == "add":
                task = input("Task to add: ")
                tasks.append(task)
                print(f"Added: {task}")
            elif action == "show":
                if len(tasks) == 0:
                    print("Your to-do list is empty.")
                else:
                    number = 1
                    for task in tasks:
                        print(f"{number}. {task}")
                        number = number + 1
            elif action == "remove":
                task = input("Task to remove: ")
                if task in tasks:
                    tasks.remove(task)
                    print(f"Removed: {task}")
                else:
                    print("That task is not on your list.")
            elif action == "back":
                break
            else:
                print("Please choose add, show, remove or back.")
    elif choice == "3":
        # Simple Calculator: takes two numbers and an operation (+, -, *, /)
        # and prints the answer, without crashing on bad input.
        try:
            first = float(input("First number: "))
            second = float(input("Second number: "))
            operation = input("Operation (+, -, *, /): ")
            if operation == "+":
                print(f"{first} + {second} = {first + second}")
            elif operation == "-":
                print(f"{first} - {second} = {first - second}")
            elif operation == "*":
                print(f"{first} * {second} = {first * second}")
            elif operation == "/":
                if second == 0:
                    print("Cannot divide by zero.")
                else:
                    print(f"{first} / {second} = {first / second}")
            else:
                print("Please choose +, -, * or /.")
        except ValueError:
            print("Please type numbers only.")
    elif choice == "4":
        print("Goodbye! Thanks for using the toolkit.")
        break
    else:
        print("Sorry, that is not on the menu. Please choose 1, 2, 3 or 4.")