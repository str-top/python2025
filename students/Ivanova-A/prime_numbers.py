while True:
        number = int(input("Введите целое положительное число: "))
        if number <= 0:
            print("Число должно быть положительным!")
        else:
            print("Это не целое число! Попробуйте ещё раз.")
            break
        
is_prime = True
if number == 1:
    is_prime = False
else:
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break
if is_prime:
    print(f"Число {number} является простым.")
else:
    print(f"Число {number} не является простым.")

print("\nРезультат FizzBuzz:")
for num in range(1, number + 1):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)
