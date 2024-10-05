import random


TASK = "Find the greatest common divisor of given numbers."


def find_gcd(a, b):  # recursion variation
    if b == 0:
        return a
    else:
        return find_gcd(b, a % b)


def get_question():
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)
    question = f'{number1} {number2}'
    correct_answer = str(find_gcd(number1, number2))
    return question, correct_answer
