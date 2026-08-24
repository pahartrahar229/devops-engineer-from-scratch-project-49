import math
import random


def generate_round():
    first = random.randint(1, 100)
    second = random.randint(1, 100)
    correct_answer = math.gcd(first, second)
    question = f'{first} {second}'
    return question, correct_answer