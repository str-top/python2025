while True:
    try:
        number = int(input("Введите целое положительное число: "))
        if number > 0:
            break 
        else:
            print("Ошибка: число должно быть положительным. Попробуйте снова.")
    else:
        print("Ошибка: введено не число. Попробуйте снова.")
is_prime = True
if number == 1:
    is_prime = False
else:
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            is_prime = False
            break
if is_prime:
    print(f"Число {number} является простым.")
else:
    print(f"Число {number} не является простым.")
print("Результат замены:")
for i in range(1, number + 1):
    if i % 3 == 0 and i % 5 == 0: 
        print("FizzBuzz", end=" ")
    elif i % 3 == 0: 
        print("Fizz", end=" ")
    elif i % 5 == 0:
        print("Buzz", end=" ")
    else: 
        print(i, end=" ")
print() 
