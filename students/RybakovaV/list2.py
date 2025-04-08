def listt():
    my_list = []
  
    while True:
        print("\nТекущий список:", my_list)
        print("\nМеню операций со списком:")
        print("1 = Добавить элемент в конец списка")
        print("2 = Удалить  элемент если он повторяется")
        print("3 = Найти индекс элемента")
        print("4 = Отсортировать список по возрастанию")
        print("5 = Развернуть список")
        choice = input("Выберите операцию (1-5): ")
        
        if choice == '1':
            element = input("Введите элемент для добавления: ")
            my_list.append(element)
            print(f"Элемент '{element}' добавлен в конец списка.")
            
        elif choice == '2':
            if not my_list:
                print("Список пуст!")
                continue
            element = input("Введите элемент для удаления: ")
            if element in my_list:
                my_list.remove(element)
                print(f"Первое вхождение элемента '{element}' удалено.")
            else:
                print(f"Элемент '{element}' не найден в списке.")
                
        elif choice == '3':
            if not my_list:
                print("Список пуст!")
                continue
            element = input("Введите элемент для поиска: ")
            if element in my_list:
                index = my_list.index(element)
                print(f"Элемент '{element}' найден на позиции {index}.")
            else:
                print(f"Элемент '{element}' не найден в списке.")
                
        elif choice == '4':
            try:
                my_list.sort()
                print("Список отсортирован по возрастанию.")
            except TypeError:
                print("Ошибка: нельзя сортировать список с разными типами данных!")
                
        elif choice == '5':
            my_list.reverse()
            print("Список развернут в обратном порядке.")
            break
        else:
            print("Неверный ввод! Пожалуйста, выберите число от 1 до 5.")

if __name__ == "__main__":
    listt()
