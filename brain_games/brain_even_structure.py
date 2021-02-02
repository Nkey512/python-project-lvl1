def even_game(func, name, levels):
    print('Answer \'yes\' if the number is even, otherwise answer \'no\'.')
    right_answers = 0
    while right_answers != levels:
        result = func()
        if result['passed']:
            print('Correct!')
            right_answers += 1
        else:
            print(
                "\'{}\' is wrong answer ;(. Correct answer was \'{}\'"
                .format(result['answer'], result['correct_answer'])
            )
            print("Let\'s try again {}".format(name))
            break
    else:
        print('Congratulations, {}!'.format(name))
