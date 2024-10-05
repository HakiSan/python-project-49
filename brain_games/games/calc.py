import random


TASK = 'What is the result of the expression?'


def get_question():
    operand1 = random.randint(1, 100)
    operand2 = random.randint(1, 10)
    operator = random.choice(["+", "-", "*"])
    question = f'{operand1} {operator} {operand2}'
    correct_answer = str(eval(question))
    return question, correct_answer