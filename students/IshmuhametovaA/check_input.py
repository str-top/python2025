while True:
    try:
        s = input("Введите строку (латинские буквы и пробелы): ")
        if not all(c.isalpha() or c.isspace() for c in s):
            raise ValueError("Только латинские буквы и пробелы!")
        s = s.upper()
        print("Строка:", s)
        
        n = int(input("Введите индекс: "))
        if abs(n) >= len(s):
            raise IndexError(f"Индекс должен быть от {-len(s)} до {len(s)-1}")
            
        print(f"Символ: '{s[n]}'")
        break
        
    except ValueError as e:
        print("Ошибка:", e)
    except TypeError:
        print("Ошибка: введите целое число!")
    except IndexError as e:
        print("Ошибка:", e)
