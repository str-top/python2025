try:
  str = input("введите какую-нибудь строку")
  for letter in str:
    if not(letter.isalpha() and letter.isascii()) and letter !=' ':
        raise ValueError('Ошибка! В этой строке должны быть только буквы и пробелы!!!')
      except ValueError:
         print('Ошибка! В этой строке не должно быть ничего кроме букв!')
        else:
    preob = str.upper()
    print(f'Преобразованная строка: {preob}')
    try:
        n = input('введи индекс своей строки')
      f not n.isdigit():
            raise TypeError('Индекс должен быть целым числом.')
    except TypeError as e:
        print(f'Ошибка: {e}')
    else:
        try:
            i = int(n)
            print(f'символ на позиции {i}: {preob[i]}')
          except IndexError:
            print('Вы ввели индекс, который не существует!!!')
