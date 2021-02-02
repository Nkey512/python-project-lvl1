#!/usr/bin/env python
def main():
    from brain_games import cli, game_structure as gs, levels
    from brain_games.games_logic import brain_even_logic as bel

    user = cli.welcome_user()
    bel.even_description()
    gs.game(bel.even_logic, user, levels.even_levels)


if __name__ == '__main__':
    main()
