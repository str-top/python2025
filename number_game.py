import random

def guess_the_number():
    secret_number = random.randint(1, 100)
    att = 0
    guessed = False

    print("загадал число от 1 до 100. Попробуй угадать его")

    while not guessed:
        user_guess = input("введите ваше предположение: ")
        if not user_guess.isdigit():
            print("пожалуйста введите целое число.")
            continue

        user_guess = int(user_guess)
        att += 1

        if user_guess < secret_number:
            print("число больше.")
        elif user_guess > secret_number:
            print("число меньше.")
        else:
            guessed = True
            print(f"ураа! ты угадал число {secret_number} за {atr} попыток.")

guess_the_number()
