# Открываем файл для чтения
with open('file.txt', 'r', encoding='utf-8') as file:
    # Читаем все строки из файла
    lines = file.readlines()
    
    # Выводим строки в обратном порядке
    for line in reversed(lines):
        print(line.strip())  # strip() убирает лишние переносы строк


with open('file.txt', 'r', encoding='utf-8') as file:
    # Читаем файл с конца (для очень больших файлов)
    for line in reversed(list(file)):
        print(line.strip())
