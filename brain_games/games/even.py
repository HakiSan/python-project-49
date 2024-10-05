import random


TASK = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_question():
    number = random.randint(1, 100)
    question = str(number)
    if number % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, correct_answer
