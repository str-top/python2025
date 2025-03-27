import re

def process_string():
    
    try:
        input_string = input("Введите строку: ")

        if not re.match("^[a-zA-Zа-яА-Я\s]*$", input_string):
            raise ValueError("Строка должна содержать только буквы и пробелы.")

        upper_string = input_string.upper()
        print("Преобразованная строка:", upper_string)

        index_str = input("Введите индекс: ")

        try:
            index = int(index_str)
        except ValueError:
            raise TypeError("Индекс должен быть целым числом.")

        if index < 0 or index >= len(upper_string):
            raise IndexError("Индекс выходит за пределы длины строки.")

        print("Символ на позиции", index, ":", upper_string[index])

    except ValueError as ve:
        print("Ошибка:", ve)
    except TypeError as te:
        print("Ошибка:", te)
    except IndexError as ie:
        print("Ошибка:", ie)

process_string()
