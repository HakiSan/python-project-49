import random
import prompt
from brain_games.cli import welcome_user
# need refactor


name = welcome_user()

def is_correct(question, answer):
    result = eval(question)
    if result == answer:
        return True
    else: return False

def main():
    num_corr_answers = 0
    print('What is the result of the expression?')
    while num_corr_answers < 3:
        operand1 = random.randint(1,100)
        operand2 = random.randint(1,10)
        operator = random.choice(['+', '-', '*'])
        question = f"{operand1} {operator} {operand2}"
        print(f"Question: {question}")
        answer = prompt.integer('Your answer: ')
        if is_correct(question, answer):
            print('Correct!')
            num_corr_answers += 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{eval(question)}'.")
            print(f"Let's try again, {name}!")
            break
    if num_corr_answers == 3:
        print(f'Congratulations, {name}!')
