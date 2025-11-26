print("Мой необычный калькулятор")
print("Команды: add, take, mul, div")
print()

a = float(input("Введи первое число: "))
b = float(input("Введи второе число: "))
command = input("Введи оператор (add, take, mul, div): ")

if command == "add":
    answer = a + b
elif command == "take":
    answer = a - b
elif command == "mul":
    answer = a * b
elif command == "div":
    if b == 0:
        answer = "Ошибка: деление на ноль"
    else:
        answer = a / b
else:
    answer = "Не знаю такой команды"

print("Результат:", answer)
