def validate_string(input_str):
    """Проверяет, что строка содержит только латинские буквы и пробелы."""
    for char in input_str:
        if not (char.isalpha() and char.isascii() or char == ' '):
            raise ValueError("Строка должна содержать только латинские буквы и пробелы")

def process_string():
    """Основная функция обработки строки."""
    try:
        # Шаг 1: Ввод и проверка строки
        input_str = input("Введите строку (только латинские буквы и пробелы): ")
        validate_string(input_str)
        
        # Шаг 2: Преобразование в верхний регистр
        upper_str = input_str.upper()
        print("Преобразованная строка:", upper_str)
        
        # Шаг 3: Ввод и проверка индекса
        try:
            n = int(input("Введите целое число (индекс символа): "))
        except ValueError:
            raise TypeError("Введенное значение должно быть целым числом")
        
        # Шаг 4: Проверка границ индекса
        if n < 0 or n >= len(upper_str):
            raise IndexError(f"Индекс должен быть от 0 до {len(upper_str) - 1}")
        
        # Шаг 5: Вывод символа
        print(f"Символ на позиции {n}:", upper_str[n])
        
    except ValueError as ve:
        print("Ошибка:", ve)
    except TypeError as te:
        print("Ошибка:", te)
    except IndexError as ie:
        print("Ошибка:", ie)

# Запуск программы
process_string()
