from random import randint
import prompt


def even_game(name, levels):
    right_answers = 0
    while right_answers != levels:
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
        print('Congratulations, {}!'.format(name))
