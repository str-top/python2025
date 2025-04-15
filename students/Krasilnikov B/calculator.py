def plus(a=2, b=2):
    return a + b


def minus(a=2, b=2):
    return a - b


def umnozh(a=2, b=2):
    return a * b


def delit(a=2, b=2):
    return a / b


def main():
    action = input(r'напишите какое нибудь простое уравнение (например: 2 + 2 или 9 / 3)')
    if '+' in action:
        parts = action.split('+')
        a = int(parts[0].strip())
        b = int(parts[1].strip())
        print(f'Результат сложения {a} и {b} будет: {int(plus(a, b))}')
    elif '-' in action:
        parts = action.split('-')
        a = int(parts[0].strip())
        b = int(parts[1].strip())
        print(f'Результат вычитания {a} и {b} будет: {int(minus(a, b))}')
    elif '*' in action:
        parts = action.split('*')
        a = int(parts[0].strip())
        b = int(parts[1].strip())
        print(f'Результат умножения {a} на {b} будет: {int(umnozh(a, b))}')
    elif '/' in action:
        parts = action.split('/')
        a = int(parts[0].strip())
        b = int(parts[1].strip())
        print(f'Результат деления {a} на {b} будет: {int(delit(a, b))}')


main()
