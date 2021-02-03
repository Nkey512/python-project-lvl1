#!/usr/bin/env python
def main():
    # from brain_games import cli, game_structure as gs, levels
    # from brain_games.games_logic import brain_gcd_logic as bgl
    from brain_games.cli import welcome_user
    from brain_games.game_structure import game
    from brain_games.levels import gcd_levels
    from brain_games.games_logic.brain_gcd_logic \
        import gcd_description, gcd_logic

    user = welcome_user()
    gcd_description()
    game(gcd_logic, user, gcd_levels)


if __name__ == '__main__':
    main()
