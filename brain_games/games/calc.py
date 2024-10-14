import random
from operator import sub, add, mul


TASK = 'What is the result of the expression?'


def calculate(sign):
    if sign == '+':
        return add
    elif sign == '*':
        return mul
    elif sign == '-':
        return sub


def get_question():
    operand1 = random.randint(1, 100)
    operand2 = random.randint(1, 10)
    sign = random.choice(["+", "-", "*"])
    question = f'{operand1} {sign} {operand2}'
    correct_answer = str(calculate(sign)(operand1, operand2))
    return question, correct_answer
