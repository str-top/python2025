# Открываем файл input.txt для чтения и numbers.txt для записи
with open('input.txt', 'r') as input_file, open('numbers.txt', 'w') as numbers_file:
    # Читаем строки из input.txt
    for line in input_file:
        # Проверяем, содержит ли строка хотя бы одну цифру
        if any(char.isdigit() for char in line):
            # Записываем строку в numbers.txt
            numbers_file.write(line)



# Открываем input.txt и читаем все строки в список
with open('input.txt', 'r') as input_file:
    lines = input_file.readlines()

# Открываем numbers.txt для записи
with open('numbers.txt', 'w') as numbers_file:
    # Перебираем строки
    for line in lines:
        # Проверяем на наличие цифр
        if any(char.isdigit() for char in line):
            # Записываем подходящие строки
            numbers_file.write(line)
