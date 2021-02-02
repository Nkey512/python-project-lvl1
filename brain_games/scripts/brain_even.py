#!/usr/bin/env python
def main():
    from brain_games import cli,\
        brain_even_structure as bes,\
        brain_even_logic as bel,\
        levels

    user = cli.welcome_user()
    bes.even_game(bel.even_logic, user, levels.even_levels)


if __name__ == '__main__':
    main()
