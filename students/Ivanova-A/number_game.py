import random

secretNum = random.randint(1, 100)
attempts = 0
max_attempts = 5

while attempts < max_attempts:
    num = int(input("Введите число: ")) 
    attempts += 1  
    if num < secretNum:
        print('Число меньше загаданного')
    elif num > secretNum:
        print('Число больше загаданного')
    else:
        print(f'Вы угадали число за {attempts} попыток!')
        break 


if attempts == max_attempts:
    print(f'Вы не смогли угадать число {secretNum}. Хорошего дня! Игра окончена.')
