def main():
    """Главная функция, обрабатывающая ввод/вывод"""
    print("Добро пожаловать в калькулятор!")
    print("Доступные операции: +, -, *, /")
    
    try:
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))
        operation = input("Выберите операцию (+, -, *, /): ")
    except ValueError:
        print("Ошибка: введены некорректные числа. Используются значения по умолчанию (5 и 2, +)")
        num1, num2, operation = 5, 2, '+'  # Значения по умолчанию
    
    result = calculate(num1, num2, operation)
    print(f"Результат: {result}")

def calculate(a, b, op='+'):
    """Выполняет математические операции"""
    if op == '+':
        return add(a, b)
    elif op == '-':
        return subtract(a, b)
    elif op == '*':
        return multiply(a, b)
    elif op == '/':
        return divide(a, b)
    else:
        print(f"Ошибка: неизвестная операция '{op}'. Выполняется сложение по умолчанию.")
        return add(a, b)  # Значение по умолчанию

def add(a, b):
    """Сложение"""
    return a + b

def subtract(a, b):
    """Вычитание"""
    return a - b

def multiply(a, b):
    """Умножение"""
    return a * b

def divide(a, b):
    """Деление"""
    try:
        return a / b
    except ZeroDivisionError:
        print("Ошибка: деление на ноль. Возвращается 0.")
        return 0  # Значение по умолчанию

if __name__ == "__main__":
    main()
