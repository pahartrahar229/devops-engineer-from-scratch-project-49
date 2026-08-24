import random


def build_sequence(start, step, length):
    return [start + index * step for index in range(length)]


def generate_round():
    length = random.randint(5, 10)
    start = random.randint(1, 20)
    step = random.randint(1, 5)

    sequence = build_sequence(start, step, length)
    hidden_index = random.randint(0, length - 1)
    correct_answer = sequence[hidden_index]

    display_sequence = sequence.copy()
    display_sequence[hidden_index] = '..'
    question = ' '.join(str(item) for item in display_sequence)

    return question, correct_answer