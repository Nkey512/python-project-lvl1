from random import randint
from math import gcd
import prompt


def gcd_description():
    print('Find the greatest common divisor of given numbers.')


def gcd_logic():
    number1 = randint(1, 99)
    number2 = randint(1, 99)
    correct_answer = gcd(number1, number2)
    print('Question: {} {}'.format(number1, number2))
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
