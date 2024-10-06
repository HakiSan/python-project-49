import random

TASK = 'What number is missing in the progression?'


def get_question():
    num_numbers = random.randint(5, 10)
    start = random.randint(1, 100)
    step = random.randrange(1, 10)
    stop = start + step * num_numbers
    question = list(range(start, stop, step))
    correct_answer = str(random.choice(question))
    question = str(question)
    question = question.replace(correct_answer, '..')
    return question, correct_answer
