dictionary = {
    'kiujyhgfvd':'jhgfd', 'kiugfvd':'jhukgmjynhtbgfd', 'kirvrujyhgfvd':'jhredgfd', 'gfkiujyhgfvd':'jhinfcgfd', 
}


def add():
    
    slovo = input('введие добовл. слово: ')
    znachenie = input(f'введите значение слова:  {slovo}')
    global dictionary
    dictionary[слово] = znachenie
    
def show():
    global dictionary
    slovo = input('введие добовл. слово: ')
    print(f'значение слова: {slovo}: {dictionary[slovo]}')
    
def delete():
    global dictionary
    slovo = input('введие добовл. слово: ')
    del dictionary[slovo]
    




while True:
    menu = '''
    выберете действие:
    1 - добавление слова
    2 - вывод значения слова
    3 - удаление слова
    '''
    vibor = input(menu)
    if vibor == '1':
        add()
    elif vibor == '2':
        show()
    elif vibor == '3':
        delete()
    
