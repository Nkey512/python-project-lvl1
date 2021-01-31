#!/usr/bin/env python
def main():
    from random import randint
    from brain_games import cli
    import prompt

    def even_game(name):
        right_answers = 0
        while right_answers != 3:
            number = randint(1, 99)
            even = not bool(number % 2)
            if even:
                correct_answer = 'yes'
            else:
                correct_answer = 'no'
            print('Question: {}'.format(number))
            answer = prompt.string('Your answer: ')
            if answer == correct_answer:
                print('Correct!')
                right_answers += 1
            else:
                print(
                    "\'{}\' is wrong answer ;(. Correct answer was \'{}\'"
                    .format(answer, correct_answer)
                )
                print("Let\'s try again {}".format(name))
                break
        else:
            print('Congratulations. {}!'.format(name))

    print('Welcome to the Brain Games!')
    user = cli.welcome_user()
    print('Hello {}'.format(user))
    print('Answer "yes" if the number is even, otherwise answer "no".')
    even_game(user)


if __name__ == '__main__':
    main()
