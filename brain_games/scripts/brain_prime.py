#!/usr/bin/env python
def main():
    # from brain_games import cli, game_structure as gs, levels
    # from brain_games.games_logic import brain_prime_logic as bpl
    from brain_games.cli import welcome_user
    from brain_games.game_structure import game
    from brain_games.levels import prime_levels
    from brain_games.games_logic.brain_prime_logic \
        import prime_description, prime_logic

    user = welcome_user()
    prime_description()
    game(prime_logic, user, prime_levels)


if __name__ == '__main__':
    main()
