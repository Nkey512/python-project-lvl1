#!/usr/bin/env python
def main():
    from brain_games import cli, brain_even_logic as bel, levels

    user = cli.welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    bel.even_game(user, levels.even_levels)


if __name__ == '__main__':
    main()
