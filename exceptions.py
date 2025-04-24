def process_numbers():
    numbers = [10, 5, 0, "abc", 3]

    for i in range(len(numbers)):
        try:
            if i > 0:
                result = numbers[i] / numbers[i - 1]
                print("Резул дел", result)
            print("доступ к элементу:", numbers[i + 1])
            print("сложение строки:", numbers[i] + 1)

        except IndexError:
            print("Ошибка: попытка доступа к несуществующему индексу.")
        except ZeroDivisionError:
            print("Ошибка: деление на ноль.")
        except TypeError:
            print("Ошибка: несовместимый тип данных.")
        except Exception:
            print("неизвестная ошибка.")

    finally:
      print("Завершение программы.")

process_numbers()
