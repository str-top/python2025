def sloj(a=0, b=0):
    return a + b

def umn(a=1, b=1):
    return a * b

def vich(a=0, b=0):
    return a - b

def razd(a=1, b=1):
    if b == 0:
        return "Ошибка: деление на ноль"
    return a / b
    
def main():
    while True:
        print(menu)
        choice = input()
        
        try:
            vvod_a = int(input('Введите первое число : ') or 0)
            vvod_b = int(input('Введите второе число : ') or 0)
        except ValueError:
            print("Неверный ввод")
            vvod_a = 0
            vvod_b = 0
        
        if choice == '1':
            result = sloj(vvod_a, vvod_b)
            print(f"Результат сложения: {result}")
        elif choice == '2':
            result = umn(vvod_a, vvod_b)
            print(f"Результат умножения: {result}")
        elif choice == '3':
            result = vich(vvod_a, vvod_b)
            print(f"Результат вычитания: {result}")
        elif choice == '4':
            result = razd(vvod_a, vvod_b)
            print(f"Результат деления: {result}")
        else:
            print("Неверный выбор. Пожалуйста, выберите действие от 1 до 4.")


menu = """
Выберите действие:
1 - сложить
2 - умножить
3 - отнять
4 - разделить
    """
if __name__ == "__main__":
    main()
