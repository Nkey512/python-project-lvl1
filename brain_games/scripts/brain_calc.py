#!/usr/bin/env python
def main():
    from brain_games import cli,\
        brain_calc_structure as bcs,\
        brain_calc_logic as bcl,\
        levels

    user = cli.welcome_user()
    bcl.calc_description()
    bcs.calc_game(bcl.calc_logic, user, levels.calc_levels)


if __name__ == '__main__':
    main()
