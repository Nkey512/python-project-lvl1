#!/usr/bin/env python
def main():
    # from brain_games import cli, game_structure as gs, levels
    # from brain_games.games_logic import brain_even_logic as bel
    from brain_games.cli import welcome_user
    from brain_games.game_structure import game
    from brain_games.levels import even_levels
    from brain_games.games_logic.brain_even_logic \
        import even_description, even_logic

    user = welcome_user()
    even_description()
    game(even_logic, user, even_levels)


if __name__ == '__main__':
    main()
