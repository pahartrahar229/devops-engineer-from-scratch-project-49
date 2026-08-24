from brain_games.engine import run_game
from brain_games.games.progression import generate_round


def main():
    description = 'What number is missing in the progression?'
    run_game(description, generate_round)


if __name__ == '__main__':
    main()