from random import randint
import prompt


def progression_description():
    print('What number is missing in the progression?')


def progression_logic():
    length = 8
    start = randint(0, 20)
    delta = randint(2, 10)
    seq = [start + delta * i for i in range(length)]
    miss = randint(0, length - 1)

    string = \
        ' '.join(map(str, seq[:miss])) + \
        ' .. ' + \
        ' '.join(map(str, seq[miss + 1:]))
    print('Question: {}'.format(string))

    correct_answer = seq[miss]
    answer = prompt.integer('Your answer: ')

    if answer == correct_answer:
        return {
            'passed': True,
            'answer': answer,
            'correct_answer': correct_answer,
        }
    else:
        return {
            'passed': False,
            'answer': answer,
            'correct_answer': correct_answer,
        }
