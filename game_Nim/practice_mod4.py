from termcolor import colored
from nim_engine import get_bunches, put_stones, is_gameover, take_from_bunch
import os

os.system('color')

put_stones()
user_number = 1
while True:
    print(colored("Текущая позиция", color='green'))
    print(colored(get_bunches(), color='green'))
    user_color = 'blue' if user_number == 1 else 'yellow'
    print(colored('Ход игрока {}'.format(user_number), color=user_color))
    pos = input(colored("Откуда берём?", color=user_color))
    qua = input(colored("Сколько берём?", color=user_color))
    step_successed = take_from_bunch(position=int(pos), quantity=int(qua))
    if step_successed:
        user_number = 2 if user_number == 1 else 1
    else:
        print(colored('Невозможный ход', color='red'))

    if is_gameover():
        break

print(colored('Выйграл игрок {}'.format(user_number), color='red'))
