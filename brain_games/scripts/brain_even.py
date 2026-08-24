from brain_games.engine import run_game
from brain_games.games.even import generate_round


def main():
    description = 'Answer "yes" if the number is even, otherwise answer "no".'
    run_game(description, generate_round)


if __name__ == '__main__':
    main()