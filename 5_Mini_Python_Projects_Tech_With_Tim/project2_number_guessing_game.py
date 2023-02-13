"""
This is done watching the video 5 Mini Python Projects - For Beginners on https://www.youtube.com/watch?v=DLn3jOsNRVE
I watched the videos and after that did the project not looking the actual codes.

25:05 | Project #2 - Number Guessing Game

---

pick a random number

then ask the user to guess this number and ask it with while.

then give feedback to the user whether it is greater or less than the number

Let's ask in which interval the useryou want to guess

tell the user how many times he did try to guess the number correctly
"""

import random


class PrintColored:
    """
    CLASS:
    Coloring the printed text in the terminal LINK:https://www.geeksforgeeks.org/print-colors-python-terminal/
    ANSI Escape Sequence is used

    :param text_to_be_colored: str - text to be colored
    :return:
    """

    def __init__(self, text_to_be_colored):
        self.text_to_be_colored = text_to_be_colored

    def red(self): print(f"\033[91m{self.text_to_be_colored}\033[00m")

    def green(self): print(f"\033[92m{self.text_to_be_colored}\033[00m")

    def yellow(self): print(f"\033[93m{self.text_to_be_colored}\033[00m")

    def light_purple(self): print(f"\033[94m{self.text_to_be_colored}\033[00m")

    def purple(self): print(f"\033[95m{self.text_to_be_colored}\033[00m")

    def cyan(self): print(f"\033[96m{self.text_to_be_colored}\033[00m")

    def light_gray(self): print(f"\033[97m{self.text_to_be_colored}\033[00m")

    def black(self): print(f"\033[98m{self.text_to_be_colored}\033[00m")


def start_the_guess(top_number):
    """
    Starting the game

    Variables:
    @random_number: int - select randomly a number between 1 to @top_number
    @user_guess: int - users' guess
    @user_already_guess: list - users' guess will be listed in here
    :param top_number: int - users picked integer to create an interval
    :return:
    """

    random_number = random.randint(1, top_number)
    user_guess = 0
    user_already_guess = []
    while random_number != user_guess:
        try:
            user_guess = int(input("What is your guess: "))
            if user_guess in user_already_guess:
                PrintColored(f"You already pick the number {user_guess}, continue to try...").yellow()
            else:
                if user_guess < random_number:
                    user_already_guess.append(user_guess)
                    user_already_guess.sort()
                    PrintColored("\u2193 Low!").red()
                    print(f"Guess list: {user_already_guess}\n")
                if user_guess > random_number:
                    user_already_guess.append(user_guess)
                    user_already_guess.sort()
                    PrintColored("\u2191 High!").red()
                    print(f"Guess list: {user_already_guess}\n")
        except:
            print("Write an integer")
    PrintColored(
        f"\u2713 Yey! After {len(user_already_guess)} time\\s try, you find the number and it was {random_number}.").green()


def main():
    """
    This is the main body, and it asks users whether they want to play or not.

    Variables:
    @user_answer: str - is the users' answer
    @top_number: int - top end which represent the interval
    :return:
    """
    while True:
        user_answer = input(
            "Do you want to play the number of guessing game? Write initial of Yes (y), No (n), Quit (q): \n").lower()
        if user_answer == "y":
            try:
                top_number = int(
                    input("In which interval you want to guess a number? Write an integer greater than zero: \n"))
                if top_number < 1:
                    print("You should write an integer greater than zero!")
                    break
                elif top_number == 1:
                    print(f"You pick {top_number} but there is no interval to guess between 1 and {top_number}!")
                    break
                else:
                    print(f"You pick {top_number} and starting the guessing game...\n")
                    start_the_guess(top_number)
                    return True
            except:
                print("Please write an integer...")
        elif user_answer == "n" or user_answer == "q":
            if user_answer == "n":
                print("Okay, you don't want to play the game and quit!")
            if user_answer == "q":
                print("You quit the game!")
            quit()
        else:
            print("Please write your decision as y, n, q...")


main()
