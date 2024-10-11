import random


TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    if number <= 1:
        return False
    i = 2
    while i <= number**0.5:
        if number % i == 0:
            return False
        i += 1
    return True


def get_question():
    number = random.randint(2, 100)
    question = str(number)
    if is_prime(number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, correct_answer
