s = input("Введите строку: ")

if not all(c.isalpha() or c == ' ' for c in s):
    print("Ошибка: Можно вводить только буквы и пробелы!")
    exit()

upper_s = s.upper()
print("Результат:", upper_s)

index = input("Введите индекс символа: ")
if not index.isdigit():
    print("Ошибка: Индекс должен быть числом!")
    exit()

index = int(index)
if index < 0 or index >= len(upper_s):
    print(f"Ошибка: Индекс должен быть от 0 до {len(upper_s) - 1}")
    exit()

print(f"Символ на позиции {index}: {upper_s[index]}")
