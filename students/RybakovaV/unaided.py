def plus(a, b):
    return (a + b)

def minus(a, b):
    return a - b

def multiply(a=1, b=1):
    return a * b

def divide(a=1, b=1):
    return a / b

def calculator():
    try:
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))
        operation = input("Введите операцию (+, -, *, /): ").strip()
    except ValueError:
        print("Ошибка: введены некорректные числа. Используются значения по умолчанию (0 и 1).")
        num1 = 0
        num2 = 1
        operation = "+"
    
    result = 0
    if operation == "+":
        result = plus(num1, num2)
    elif operation == "-":
        result = minus(num1, num2)
    elif operation == "*":
        result = multiply(num1, num2)
    elif operation == "/":
        result = divide(num1, num2)
    else:
        print("Ошибка: неизвестная операция. Используется сложение по умолчанию.")
        result = add(num1, num2)
    print(f"Результат: {result}")
if __name__ == "__main__":
    calculator()
