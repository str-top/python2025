
try:
    user_vvod = input('введенная строка содержит только буквы латинского алфавита (заглавные или строчные) и пробелы. ')
except ValueError as e:
        print(f'Ошибка {e}')
        
user_vvod = input('введите строку : ')
upper_case_string = user_vvod.upper()
print("Строка в верхнем регистре:", upper_case_string)


example_string = "Hello World"
try:
    num = input('введите челое число n, которое будет обозначать индекс символа в строке: ')
    num = int(num)
    # Проверяем, что индекс находится в пределах длины строки
    if num < 0 or num >= len(example_string):
        raise IndexError("Индекс выходит за пределы строки.")
        
    print(f"Символ по индексу {num}: {example_string[num]}")
        
except ValueError:
    print('Ошибка число должнго быть целым ')
except IndexError as e:
    print(f'Ошибка: {e}')
    
