from random import randint
from time import time

if __name__ == '__main__':

    # Спрашивает имя пользователя
    user_name = input('Enter your name\n').title()

    # Приветствие
    print(f'Hello {user_name}!\n Here is your examples with division\n You have 5 minutes to decide them.\n')

    # список для примеров
    examples = []
    # писок с ответами
    answers = []


    def expresisons() -> dict:
        """
        Функция создаёт примеры из рандомно взятых чисел из определённого диапазона, отфильтровывает
        и заносит их в список и отдельно ответы в другой список, после чего склеивает их в словарь.
        :return:
        """
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
    # print(ex_dict)

    # счётчик ответов
    score = 0

    # счётчик вопросов
    answer_count = 0

    # фиксатор времени
    start = time()

    for key, value in ex_dict.items():
        user_answer = input(f'{key} ')

        # остановка программы
        if user_answer in ('stop', 'стоп'):
            print("You stop the game. Let's see your results...\n")
            break
        # проверка ответов
        elif user_answer == value:
            score += 1
            answer_count += 1
            print('The answer is correct!')
        else:
            answer_count += 1
            print('Wrong answer!')
            continue

    # подсчёт вреемни на решение
    ending = time()
    time_counter = str((ending - start) / 60)

    # результаты
    print(f'{user_name}, your time is {time_counter[:4]} min.\nCorrect answers are {score} from {answer_count}.')

    if score == answer_count and score >= 10:
        print(f'Good job, {user_name}! You done vell!')
