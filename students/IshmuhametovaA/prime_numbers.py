def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def fizz_buzz(n):
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

def main():
    while True:
        try:
            number = int(input("Введите целое положительное число: "))
            if number > 0:
                break
            else:
                print("Число должно быть больше нуля. Попробуйте снова.")
        except ValueError:
            print("Ошибка: введите целое число.")
          
    if is_prime(number):
        print(f"Число {number} является простым.")
    else:
        print(f"Число {number} не является простым.")
      
    print("Результат FizzBuzz:")
    fizz_buzz(number)

main()
