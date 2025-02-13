# Таблица умножения
print("Таблица умножения".center(50))
print("-" * 54)

# Вывод заголовка
print("   ", end="")
for i in range(1, 11):
    print(f"{i:4}", end=" ")
print("\n" + "-" * 54)

# Вывод строк
for i in range(1, 11):
    print(f"{i:2} |", end="")  # Заголовок строки
    for j in range(1, 11):
        print(f"{i * j:4}", end=" ")
    print()  # Новая строка
