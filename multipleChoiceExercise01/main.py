"""
Python for Absolute Beginners from freecodecamp. You can reach via the link: https://youtu.be/rfscVS0vtbw?t=14257

Building a Multiple Choice Quiz (without looking the example)
Yes, I watch the video couple of times but this exercise created not looking the video.

"""
from multipleChoiceExercise01.Questions import Questions


def main():
    """
    This the main function will store variables in it

    Variables:
    @questions_prompts: list - This list will contain the questions asked for users to answer.
    @questions: list - This will contain question objects

    :return: This is main function call the main
    """

    questions_prompts = [
        "What is two to the third power?\na) 5\nb) 6\nc) 8\nd) 9\n\nYour choice: ",
        "\nEvaluate the expression 5x\u00b3 if x = 4\na) 40\nb) 80\nc) 160\nd) 320\n\nYour choice: ",
        "\nEvaluate the expression x\u00b3 if x = -4\na) -8\nb) -4\nc) 0\nd) 4\n\nYour choice: "
    ]

    questions = [
        Questions(questions_prompts[0], "c"),
        Questions(questions_prompts[1], "d"),
        Questions(questions_prompts[2], "b"),
    ]

    run_quiz(questions)


def run_quiz(questions):
    """
    It will ask users to input their answers

    Variables:
    @score: int - it is the users' score how many correct answers they did

    :param questions: list - it will send to the func by user
    :return: it will give  the result
    """
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print(f"\nYou did correct {score} out of {str(len(questions))}")


main()
