import random

TASK = 'What number is missing in the progression?'


def get_question():
    num_numbers = random.randint(5, 10)
    start = random.randint(1, 100)
    step = random.randrange(1, 10)
    progression = [start + step * i for i in range(num_numbers)]
    missing_element = random.randint(0, num_numbers - 1)
    correct_answer = str(progression[missing_element])
    progression[missing_element] = '..'
    question = ' '.join(str(x) for x in progression)
    return question, correct_answer
