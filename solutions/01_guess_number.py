"""
Generate a random number between 1 and 9 (including 1 and 9).
Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.
"""
import random


def guess_number():
    number_to_guess = random.choice(range(10))
    current_number = None

    while current_number != number_to_guess:
        try:
            current_number = int(input("Pick a number between 1-9: "))
            if current_number == number_to_guess:
                print("Bravo!!!")
            elif current_number < number_to_guess:
                print("Too low")
            else:
                print("Too high")
        except (TypeError, ValueError):
            print("Invalid number")


guess_number()
