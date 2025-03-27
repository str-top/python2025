def main():
    my_list = []
    
    while True:
        print("\nТекущий список:", my_list)
        print("1. Добавить элемент в конец списка")
        print("2. Удалить первый найденный элемент по значению")
        print("3. Найти индекс элемента")
        print("4. Отсортировать список по возрастанию")
        print("5. Развернуть список")
        print("6. Вывести список")
        print("7. Выход")
        
        choice = input("Выберите операцию (1-7): ")
        
        if choice == '1':
            # Добавление элемента
            element = input("Введите элемент для добавления: ")
            try:
                # Пробуем преобразовать в число, если возможно
                element = int(element)
            except ValueError:
                try:
                    element = float(element)
                except ValueError:
                    pass  # Оставляем как строку, если не число
            my_list.append(element)
            print(f"Элемент {element} добавлен.")
            
        elif choice == '2':
            # Удаление элемента
            if not my_list:
                print("Список пуст!")
                continue
            element = input("Введите элемент для удаления: ")
            try:
                # Пробуем преобразовать в число для поиска
                try:
                    element = int(element)
                except ValueError:
                    try:
                        element = float(element)
                    except ValueError:
                        pass  # Оставляем как строку, если не число
                
                if element in my_list:
                    my_list.remove(element)
                    print(f"Первое вхождение элемента {element} удалено.")
                else:
                    print("Элемент не найден в списке.")
            except ValueError:
                print("Ошибка при удалении элемента.")
                
        elif choice == '3':
            # Поиск индекса
            if not my_list:
                print("Список пуст!")
                continue
            element = input("Введите элемент для поиска: ")
            try:
                # Пробуем преобразовать в число для поиска
                try:
                    element = int(element)
                except ValueError:
                    try:
                        element = float(element)
                    except ValueError:
                        pass  # Оставляем как строку, если не число
                
                if element in my_list:
                    index = my_list.index(element)
                    print(f"Элемент {element} найден на позиции {index}.")
                else:
                    print("Элемент не найден в списке.")
            except ValueError:
                print("Ошибка при поиске элемента.")
                
        elif choice == '4':
            # Сортировка
            try:
                my_list.sort()
                print("Список отсортирован по возрастанию.")
            except TypeError:
                print("Невозможно отсортировать - список содержит элементы разных типов.")
                
        elif choice == '5':
            # Разворот списка
            my_list.reverse()
            print("Список развернут.")
            
        elif choice == '6':
            # Вывод списка
            print("Текущий список:", my_list)
            
        elif choice == '7':
            # Выход
            print("Завершение программы.")
            break
            
        else:
            print("Неверный ввод. Пожалуйста, выберите число от 1 до 7.")

if __name__ == "__main__":
    main()
