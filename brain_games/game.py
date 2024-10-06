import prompt
from brain_games.cli import welcome_user


def run_game(game):
    num_correct_answers = 3
    name = welcome_user()
    print(game.TASK)
    while num_correct_answers > 0:
        question, correct_answer = game.get_question()
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')
        if answer == correct_answer:
            print('Correct!')
            num_correct_answers -= 1
        else:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'. "
                  f"Let's try again, {name}!")
            break
        if num_correct_answers == 0:
            print(f'Congratulations, {name}!')
