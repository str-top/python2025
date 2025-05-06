def plus(x=0, y=0):
    return x + y

def minus(x=0, y=0):
    return x - y

def umnoj(x=1, y=1):
    return x * y

def delen(x=1, y=1):
    if y == 0:
        print("Ошибка")
        return 1
    return x / y
def main():
    print("калькулятор!")
    
    try:
        num1 = float(input("ведите первое число ") or 0)
    except ValueError:
        print("неверный ввод")
        num1 = 0

    try:
        num2 = float(input("Введите второе число") or 0)
    except ValueError:
        print("Неверный ввод.")
        num2 = 0

    operation = input("Выберите операцию (+, -, *, /): ")

    if operation == '+':
        result = plus(num1, num2)
    elif operation == '-':
        result = minus(num1, num2)
    elif operation == '*':
        result = umnoj(num1, num2)
    elif operation == '/':
        result = delen(num1, num2)
    else:
        print("Неверная операция")
        result = plus(num1, num2)

    print(f"Результат: {result}")
