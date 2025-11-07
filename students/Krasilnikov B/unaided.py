num1 = int(input("Введи первое число: "))
operation = input("Какую операцию сделать? (ъ, ё, л, р): ")
num2 = int(input("Введи второе число: "))


if operation == "ъ":
    result = num1 + num2
    print(f"Результат: {num1} ъ {num2} = {result}")
    
elif operation == "ё":
    result = num1 - num2
    print(f"Результат: {num1} ё {num2} = {result}")
    
elif operation == "л":
    result = num1 * num2
    print(f"Результат: {num1} л {num2} = {result}")
    
elif operation == "р":
    result = num1 / num2
    print(f"Результат: {num1} р {num2} = {result}")
