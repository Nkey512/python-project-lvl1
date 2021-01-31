#!/usr/bin/env python
def main():
    from brain_games import cli
    print('Welcome to the Brain Games!')
    print('Hello, {}!'.format(cli.welcome_user()))


if __name__ == '__main__':
    main()
