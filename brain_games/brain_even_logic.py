from random import randint
import prompt


def even_logic():
    number = randint(1, 99)
    even = not bool(number % 2)
    if even:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    print('Question: {}'.format(number))
    answer = prompt.string('Your answer: ')
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
