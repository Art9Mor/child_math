from random import randint
from time import time

if __name__ == '__main__':

    user_name = input('Enter your name\n').title()
    print(f'Hello {user_name}!\n Here is your examples with division\n You have 5 minutes to decide.\n')

    examples = []
    answers = []


    def expresisons() -> dict:
        count = 0
        while count < 30:
            x = randint(1, 1000)
            y = randint(1, 100)
            z = x / y
            if x / y == x // y and count < 30 and x / y != 1 and y != 1:
                count += 1
                examples.append(f'{x} : {y} =')
                answers.append(str(int(z)))
                continue
        exe_dict = dict(zip(examples, answers))
        return exe_dict


    ex_dict = expresisons()
    print(ex_dict)
    score = 0
    answer_count = 0

    counter = 1

    start = time()

    for key, value in ex_dict.items():
        user_answer = input(f'{key} ')
        if user_answer in ('stop', 'стоп'):
            print("You stop the game. Let's see your results...\n")
            break
        elif user_answer == value:
            score += 1
            answer_count += 1
            print('The answer is correct!')
        else:
            answer_count += 1
            print('Wrong answer!')
            continue

    ending = time()
    time_counter = str((ending - start) / 60)

    print(f'{user_name}, your time is {time_counter[:4]} min.\nCorrect answers are {score} from {answer_count}.')

    if score == answer_count and score >= 10:
        print(f'Good job, {user_name}! You done vell!')
