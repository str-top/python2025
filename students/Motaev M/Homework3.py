def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
while True:
    try:
        num = int(input("Введите целое положительное число: "))
        if num > 0:
            break
        else:
            print("Число должно быть положительным. Пожалуйста, повторите ввод.")
    except ValueError:
        print("Введено не число. Пожалуйста, повторите ввод.")
if is_prime(num):
    print(f"{num} - простое число.")
else:
    print(f"{num} - не простое число.")
for i in range(1, num + 1):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
