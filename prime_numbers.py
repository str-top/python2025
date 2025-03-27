while True:
    try:
        num = int(input("введите число больше нуля "))
        if num > 0:
            print(f"ты ввел число: {num}")
            break
        else:
            print("число должно быть больше нуля попробуйте снова")
    except ValueError:
        print("некорректный ввод пж введите число")

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

try:
    number = int(input("ведите целое число "))
    if is_prime(number):
        print(f"{number} является простым числом")
    else:
        print(f"{number} не является простым числом")
except ValueError:
    print("некорректный ввод пж введите целое число")
