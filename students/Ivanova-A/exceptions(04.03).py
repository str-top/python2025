list = [10, 5, 0, "abc", 3]

try:
    print(5/0)
    print(list[5])
    print(int(list[3]))
except ZeroDivisionError:
    print("НА НОЛЬ ДЕЛИТЬ НЕЛЬЗЯ")
except IndexError:
    print("такого индекса нет в списке")
except ValueError:
    print('Не коректный тип данных')
finally:
    print('Программа завершена')
