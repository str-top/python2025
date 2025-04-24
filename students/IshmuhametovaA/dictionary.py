dictionary = {\
'аборвалс' : 'собачье сердце', 'пугна' : 'живой скелет',\
'абоба' : 'инопрешеленец', 'эпимикард' : 'красталл чего-либо',\
'амням' : 'мотоцикл с крыльями', 'аааааа' : 'ааааа', 'коулдплюс' : 'абракадабра',\
'налфуми' : 'иватани'
}

def add():
    slovo = input("Введите добавляемое слово")
    znachenie = input(f"Введите значение слова {slovo} :")
    global dictionary
    dictionary[slovo] = znachenie
def show():
    global dictionary
    slovo = input("Введите слово:")
    print(f"Значение слова {slovo}: {dictionary[slovo]}")
def delete():
    global dictionary
    slovo = input("Вваедите слово")
    del dictionary[slovo]

while True:
    menu = """
    Выберите действие:
    1 - добавление слова
    2 - вывод значение
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
        print("не верная команда.")
