#!/usr/bin/env python
def main():
    # from brain_games import cli, game_structure as gs, levels
    # from brain_games.games_logic import brain_calc_logic as bcl
    from brain_games.cli import welcome_user
    from brain_games.game_structure import game
    from brain_games.levels import calc_levels
    from brain_games.games_logic.brain_calc_logic \
        import calc_description, calc_logic

    user = welcome_user()
    calc_description()
    game(calc_logic, user, calc_levels)


if __name__ == '__main__':
    main()
