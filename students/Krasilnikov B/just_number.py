# TASK 1
a = int(input("Введите число для проверки простое оно или нет "))
while a <= 0:
    a=int(input('введи целое число не меньше 1 для проверки простое оно или нет'))

# TASK 2
if a == 1:
    print(f'число {a} не простое')
elif a > 2 :
    for b in range(2, int(a ** 0.5) + 1):
        if a % b == 0:
            print(f'число {a} не простое')
            break
        else:
            print(f'число {a} простое')
            break
# TASK 3
for c in range(1,a):
    if c % 3 == 0 and c % 5 == 0: 
        print('FizzBuzz',c)
    elif c % 3 == 0:
        print('Fizz',c)
    elif c % 5 == 0:
        print('Buzz',c)
    else:
        print(c)
    
    
    
