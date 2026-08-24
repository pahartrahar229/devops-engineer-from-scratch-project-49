import prompt

ROUNDS_COUNT = 3


def run_game(description, generate_round):
    from brain_games.cli import welcome_user

    name = welcome_user()
    print(description)

    for _ in range(ROUNDS_COUNT):
        question, correct_answer = generate_round()
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')

        if answer == str(correct_answer):
            print('Correct!')
        else:
            print(
                f"'{answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'."
            )
            print(f"Let's try again, {name}!")
            return

    print(f'Congratulations, {name}!')