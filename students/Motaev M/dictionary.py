dictionary = {'аборвалс':'Собачье сердце', 'пугна':'Живой скелет',
'абоба':'инопрeшeленец', 'эпимикард':'кристалл чего-либо',
'амням':'Можно было а бы', 'Аааааа':'Аааааа', 'Налфуме':'иватани', 'коулдплюс':'абракадабра'}

def add():
    slovo = input('Введите добавляемое слово: ')
    znachenie = input(f'Введите значение слова {slovo}')
    global dictionary
    dictionary[slovo] = znachenie

def show():
    slovo = input('Введите слово: ')
    print(f'Значение слова {slovo}:{dictionary[slovo]}')

def delete():
    slovo = input('Введите слово: ')
    del dictionary[slovo]

while True:
    menu = """
Выберите действие:
1 - добавление слова
2 - вывод значения слова
3 - удаление слова
    """
    vibor = input(menu)
    if vibor == '1':
        add()
    elif vibor == '2':
        show()
    elif vibor == '3':
        delete()
    else:
        print('Неверная команда')
