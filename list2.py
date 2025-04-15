my_list = []

while True:
    print("\nВыберите операцию:")
    print("1. Добавить элемент в список")
    print("2. Удалить элемент из списка")
    print("3. Найти индекс элемента")
    print("4. Отсортировать список")
    print("5. Развернуть список")
    print("6. Вывести список")
    print("7. Выход")

    choice = input("Введите номер операции: ")

    if choice == '1':
        element = input("Введите элемент для добавления: ")
        my_list.append(element)
        print(f"Элемент '{element}' добавлен в список.")

    elif choice == '2':
        element = input("Введите элемент для удаления: ")
        if element in my_list:
            my_list.remove(element)
            print(f"Элемент '{element}' удален из списка.")
        else:
            print(f"Элемент '{element}' не найден в списке.")

    elif choice == '3':
        element = input("Введите элемент для поиска индекса: ")
        if element in my_list:
            index = my_list.index(element)
            print(f"Индекс элемента '{element}': {index}.")
        else:
            print(f"Элемент '{element}' не найден в списке.")

    elif choice == '4':
        my_list.sort()
        print("Список отсортирован по возрастанию.")

    elif choice == '5':
        my_list.reverse()
        print("Список развернут.")

    elif choice == '6':
        print("Текущий список:", my_list)

    elif choice == '7':
        print("Выход из программы.")
        break

    else:
        print("Неверный ввод, попробуйте снова.")
