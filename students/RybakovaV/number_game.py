import random

def guess_number():
    secret_number = random.randint(1, 100)
    attempts = 0 

    print("Добро пожаловать в игру 'Угадай число'!")
    print("Я загадал число от 1 до 100. Попробуй угадать!")

    while True:
        
        try:
            guess = int(input("Введите ваше число: "))
        except ValueError:
            print("Пожалуйста, введите целое число.")
            continue

        attempts += 1 

        if guess < secret_number:
            print("Загаданное число больше.")
        elif guess > secret_number:
            print("Загаданное число меньше.")
        else:
            print(f"Поздравляю! Вы угадали число за {attempts} попыток.")
            break
guess_number()
