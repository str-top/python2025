def process_list(numbers):
    try:
        for i in range(len(numbers)):
            if i > 0:
                result = numbers[i] / numbers[i - 1]
                print(f"Результат деления {numbers[i]} на {numbers[i - 1]}: {result}")
            
            if i == len(numbers):
                print(numbers[i + 1]) 

    except IndexError:
        print("Ошибка: обращение к несуществующему индексу.")
    except ZeroDivisionError:
        print("Ошибка: деление на ноль.")
    except TypeError:
        print("Ошибка: некорректный тип данных.")
    except Exception as e:
        print(f"Неожиданная ошибка: {e}")
    finally:
        print("Программа завершена.")

numbers = [10, 5, 0, "abc", 3]

process_list(numbers)
