#!/usr/bin/env python
def main():
    from brain_games import cli, game_structure as gs, levels
    from brain_games.games_logic import brain_gcd_logic as bgl

    user = cli.welcome_user()
    bgl.gcd_description()
    gs.game(bgl.gcd_logic, user, levels.gcd_levels)


if __name__ == '__main__':
    main()
