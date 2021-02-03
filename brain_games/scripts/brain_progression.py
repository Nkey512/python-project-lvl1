#!/usr/bin/env python
def main():
    from brain_games import cli, game_structure as gs, levels
    from brain_games.games_logic import brain_progression_logic as bpl

    user = cli.welcome_user()
    bpl.progression_description()
    gs.game(bpl.progression_logic, user, levels.progression_levels)


if __name__ == '__main__':
    main()
