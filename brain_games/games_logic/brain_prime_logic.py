from random import randint
import prompt


def prime_description():
    print('Answer \'yes\' if given number is prime. Otherwise answer \'no\'.')


def prime_logic():  # noqa: C901
    number = randint(1, 99)

    def prime_test(n):
        if n < 2:
            return False
        if n in (2, 3, 5, 7):
            return True
        if n in (1, 4, 6, 8, 9):
            return False
        if n % 2 == 0:
            return False
        i = 3
        while i ** 2 <= n:
            if n % i == 0:
                return False
            i += 2
        return True

    if prime_test(number):
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
