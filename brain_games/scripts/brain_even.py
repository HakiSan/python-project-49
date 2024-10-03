import random
import prompt
from brain_games.cli import welcome_user


name = welcome_user()

def is_correct(question, answer):
    if answer == is_even(question):
        return True
    else:
        return False

def is_even(question):
    if question%2 == 0:
        return 'yes'
    else:
        return 'no'

def main():
    num_corr_answers = 0
    print('Answer "yes" if the number is even, otherwise answer "no".')
    while num_corr_answers < 3:
        question = random.randint(1, 100)
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')
        if is_correct(question, answer):
            print('Correct!')
            num_corr_answers += 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{is_even(question)}'.")
            print(f"Let's try again, {name}!")
            break
    if num_corr_answers == 3:
        print(f'Congratulations, {name}!')
