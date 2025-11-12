num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))
operator = input("Введите оператор (plus, minus, umnojenie, delenie): ")

if operator == "plus":
    itog = num1 + num2
elif operator == "minus":
    itog = num1 - num2
elif operator == "umnojenie":
    itog = num1 * num2
elif operator == "delenie":
    if num2 != 0:
        itog = num1 / num2
    else:
        itog = "Ошибка: деление на ноль"
else:
    itog = "Некорректный оператор"
print("Результат:", itog)
