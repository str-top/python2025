def main():
    lst = []
    while True:
        print(f"\nТекущий список: {lst}")
        print("1. Добавить элемент")
        print("2. Удалить элемент")
        print("3. Найти индекс")
        print("4. Сортировать")
        print("5. Развернуть")
        print("6. Вывести")
        print("7. Выход")
        
        choice = input("Выберите операцию: ")
        
        if choice == '1':
            lst.append(input("Введите элемент: "))
        elif choice == '2':
            if item := input("Введите элемент для удаления: "):
                try: lst.remove(item)
                except: print("Элемент не найден!")
        elif choice == '3':
            if item := input("Введите элемент для поиска: "):
                try: print(f"Индекс: {lst.index(item)}")
                except: print("Элемент не найден!")
        elif choice == '4':
            try: lst.sort()
            except: print("Ошибка сортировки!")
        elif choice == '5':
            lst.reverse()
        elif choice == '6':
            print(f"\nСписок: {lst}")
        elif choice == '7':
            break
        else:
            print("Неверный ввод!")

if __name__ == "__main__":
    main()
