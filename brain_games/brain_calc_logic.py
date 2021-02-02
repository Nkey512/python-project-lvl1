from random import randint, choice
import prompt
import operator as op


def calc_description():
    print('What is the result of the expression?')


def calc_logic():
    number1 = randint(1, 99)
    number2 = randint(1, 99)
    operators = {'+': op.add, '-': op.sub, '*': op.mul}
    action = choice(tuple(operators.keys()))
    correct_answer = operators[action](number1, number2)
    print('Question: {} {} {}'.format(number1, action, number2))
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
