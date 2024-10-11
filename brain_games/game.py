import prompt


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


WIN = 3


def run_game(game):
    score = 0
    name = welcome_user()
    print(game.TASK)
    while score < WIN:
        question, correct_answer = game.get_question()
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')
        if answer == correct_answer:
            print('Correct!')
            score += 1
        else:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'. "
                  f"Let's try again, {name}!")
            break
        if score == WIN:
            print(f'Congratulations, {name}!')
