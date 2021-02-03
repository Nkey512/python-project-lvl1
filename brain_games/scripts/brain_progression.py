#!/usr/bin/env python
def main():
    # from brain_games import cli, game_structure as gs, levels
    # from brain_games.games_logic import brain_progression_logic as bpl
    from brain_games.cli import welcome_user
    from brain_games.game_structure import game
    from brain_games.levels import progression_levels
    from brain_games.games_logic.brain_progression_logic \
        import progression_description, progression_logic

    user = welcome_user()
    progression_description()
    game(progression_logic, user, progression_levels)


if __name__ == '__main__':
    main()
