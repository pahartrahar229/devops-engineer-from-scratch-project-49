import random

DESCRIPTION = 'What is the result of the expression?'

OPERATIONS = ('+', '-', '*')


def generate_round():
    first = random.randint(1, 100)
    second = random.randint(1, 100)
    operation = random.choice(OPERATIONS)

    match operation:
        case '+':
            correct_answer = first + second
        case '-':
            correct_answer = first - second
        case '*':
            correct_answer = first * second

    question = f'{first} {operation} {second}'
    return question, correct_answer