import random


TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    if number <= 1:
        return 'no'
    i = 2
    while i <= number**0.5:
        if number % i == 0:
            return 'no'
        i += 1
    return 'yes'


def get_question():
    number = random.randint(2, 100)
    question = str(number)
    correct_answer = is_prime(number)
    return question, correct_answer
