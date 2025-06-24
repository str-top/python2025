my_list = []

def show_list():
    if not my_list:
        print("Список пуст!")
    else:
        print("Текущий список:", my_list)

while True:
    print("\nМеню операций со списком:")
    print("1. Добавить элемент в конец списка")
    print("2. Удалить элемент (первое вхождение)")
    print("3. Найти индекс элемента")
    print("4. Отсортировать список по возрастанию")
    print("5. Развернуть список")
    print("6. Вывести список")
    print("7. Выход")

    choice = input("Выберите операцию (1-7): ")

    if choice == "1":
        element = input("Введите элемент для добавления: ")
        my_list.append(element)
        print(f"Элемент '{element}' добавлен в список.")
        show_list()

    elif choice == "2":
        if not my_list:
            print("Список пуст!")
            continue
        element = input("Введите элемент для удаления: ")
        if element in my_list:
            my_list.remove(element)
            print(f"Первое вхождение элемента '{element}' удалено.")
        else:
            print("Элемент не найден в списке.")
        show_list()

    elif choice == "3":
        if not my_list:
            print("Список пуст!")
            continue
        element = input("Введите элемент для поиска: ")
        if element in my_list:
            index = my_list.index(element)
            print(f"Элемент '{element}' найден на позиции {index}.")
        else:
            print("Элемент не найден в списке.")
        show_list()

    elif choice == "4":
        if not my_list:
            print("Список пуст!")
            continue
        my_list.sort()
        print("Список отсортирован по возрастанию.")
        show_list()

    elif choice == "5":
        if not my_list:
            print("Список пуст!")
            continue
        my_list.reverse()
        print("Список развернут в обратном порядке.")
        show_list()

    elif choice == "6":
        show_list()

    elif choice == "7":
        print("Выход из программы.")
        break

    else:
        print("Неверный выбор. Пожалуйста, введите число от 1 до 7.")
