def addition(num1, num2):
    num3 = num1 + num2
    print(f"Сумма заданых вами чисел равна {num3}")

def subtraction(num1, num2):
    num3 = num1 - num2
    print(f"Разность заданых вами чисел равна {num3}")

def multiplication(num1, num2):
    num3 = num1 * num2
    print(f"Произведение заданых вами чисел равно {num3}")

def division(num1, num2):
    if num2 == 0:
        print("На ноль делить нельзя")
    else:
        num3 = num1 / num2
        print(f"Частное заданых вами чисел равно {num3}")

def calculator():
    while True:
        try:
            num1 = float(input("Введите первое число: "))
            num2 = float(input("Введите второе число: "))
        except ValueError:
            print("Пожалуйста, введите числа")
            continue
            
        menu = """
        Введите операцию
        1 - сложение
        2 - вычитание
        3 - умножение
        4 - деление
        """
        choice = input(menu)
        if choice == '1':
            addition(num1, num2)
        elif choice == '2':
            subtraction(num1, num2)
        elif choice == '3':
            multiplication(num1, num2)
        elif choice == '4':
            division(num1, num2)
        else:
            print("Неверный выбор операции")

calculator()
