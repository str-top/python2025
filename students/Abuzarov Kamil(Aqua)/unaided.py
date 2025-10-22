def calculate(num1, operator, num2):
    if operator == '!@':  # Пример: сложение на 3
        return num1 + 3
    elif operator == '#$':  # Пример: умножение на 2
        return num1 * 2
    elif operator == '%^':  # Пример: возведение в степень 2
        return num1 ** 2
    elif operator == '&*':  # Пример: вычитание 5
        return num1 - 5
    else:
        return "Неизвестный оператор"

# Основной цикл программы
while True:
    try:
        num1 = float(input("Введите первое число: "))
        operator = input("Введите оператор (!@, #$, %^, &*): ")
        num2 = float(input("Введите второе число: "))

        result = calculate(num1, operator, num2)
        print(f"Результат: {result}")
    except ValueError:
        print("Пожалуйста, введите число.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")
    
    again = input("Продолжить? (да/нет): ")
    if again.lower() != 'да':
        break
