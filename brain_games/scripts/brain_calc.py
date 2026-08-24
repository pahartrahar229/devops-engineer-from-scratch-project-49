from brain_games.engine import run_game
from brain_games.games.calc import generate_round


def main():
    description = 'What is the result of the expression?'
    run_game(description, generate_round)


if __name__ == '__main__':
    main()