num1 =int(input("Введите первое число"))
num2 =int(input("Введите второе число"))
if type(num1) != int or type(num2) != int:
    print("ВВЕДИТЕ ЧИСЛО")
while True:
    choise =input("""В данном калькуляторе
        стандартные знаки вычисления заменены на выдуманные
        *=!, /=?, -= #, +=@
        Введите нужную цифру:
        1- num1!num2(Умножение)
        2- num1?num2(Деление)
        3- num1#num2(Вычитание)
        4- num1@num2(Сложение)
        5- Выход""")
    if choise == '1':
        num = num1 * num2
        print(num)
    if choise == '2':
        num = num1 / num2
        print(num)
        if num2 == 0:
            print("НА НОЛЬ НЕЛЬЗЯ ДЕЛИТЬ")
    if choise == "3":
        num = num1 - num2
        print(num)
    if choise == "4":
        num = num1 + num2
        print(num)
    if choise == "5":
        break
