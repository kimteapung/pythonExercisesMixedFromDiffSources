"""
This is Question class with

"""


class Questions:
    """
    Question class will contain question objects
    :param prompt: str - question prompt by the user
    :param answer: str - correct answer for a question
    """

    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer
