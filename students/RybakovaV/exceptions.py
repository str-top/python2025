numbers = [10, 5, 0, "abc", 3]
try:
    for i in range(1, len(numbers)):
        try:
            result = numbers[i] / numbers[i-1]
            print(f"Результат деления {numbers[i]} на {numbers[i-1]}: {result}")
        except ZeroDivisionError:
            print(f"Ошибка: Деление на ноль при обработке элементов {numbers[i]} и {numbers[i-1]}")
        except TypeError:
            print(f"Ошибка: Некорректный тип данных при обработке элементов {numbers[i]} и {numbers[i-1]}")
    try:
        print(f"Элемент с индексом 10: {numbers[10]}")
    except IndexError:
        print("Ошибка: Обращение к несуществующему индексу")
    try:
        invalid_operation = numbers[3] + numbers[0]
    except TypeError:
        print("Ошибка: Некорректный тип данных для операции сложения")
except Exception as e:
    print(f"Неожиданная ошибка: {e}")
finally:
    print("Программа завершена.")
