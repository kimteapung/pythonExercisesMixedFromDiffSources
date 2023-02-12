"""
This is done watching the video 5 Mini Python Projects - For Beginners on https://www.youtube.com/watch?v=DLn3jOsNRVE
I watched the videos and after that did the project not looking the actual codes.
"""


def run_the_game():
    """
    This is the function start the game.

    Variables:
    @questions_list: list - it contains the question as tuple with the question's answer
    @correct_score: int - will count the correct answer
    @user_answer: str - it is the user answer
    @ordering_question: int - order the questions
    :return:
    """
    questions_list = [
        (
            "The library at Lenape Elementary School has 2/5 as many fiction books as nonfiction books. There are 56 books in the school library. How many books are fiction books?",
            16),
        (
            "A library has 12,500 fiction books and 19,000 nonfiction books. Currently, 2/5 of the fiction books are checked out, and 2/5 of the nonfiction books are checked out. Of the books checked out, only 1/10 are due back this week. How many books are due this week?",
            1260),
        ("If three cats eat three mice in three minutes, after which time 90 cats eat 90 mice?", 3),
        ("Leslie bought 8 same chocolates for 16 Eur. How many euros will he pay for 25 chocolates?", 50),
        ("How many times can you subtract the number 4 from the number 64?", 1)
    ]
    correct_score = 0
    ordering_question = 0
    for question in questions_list:
        ordering_question += 1
        print(f"Question {ordering_question}: {question[0]}")
        user_answer = str(input("Your answer: ")).lower()
        if user_answer == str(question[1]):
            correct_score += 1
            print("\u2713 CORRECT\n")
        else:
            print("\u2717 INCORRECT!\n")
    print(f"You did {correct_score} correct out of {len(questions_list)} questions.")


def main():
    """
    This is the main body, and it asks users whether they want to play or not.

    Variables:
    @user_answer: str - is the users' answer
    :return:
    """
    user_answer = input("Do you want to play math quiz game? (Y/N)\n").lower()
    if user_answer == "y":
        run_the_game()
    else:
        quit()


main()
