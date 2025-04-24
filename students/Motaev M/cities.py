city_list = ['Москва','Питер']
city_dict = {'Москва':'Столица'}
city_tuple = ('Москва',)
city_set = {'Москва'}

def sort():
    global city_lis
    global city_dict
    global city_tuple
    global city_set
    
    city_list = sorted(city_list, key=lambda x: len(x))
    city_dict = sorted(city_dict, key=lambda x: len(x))
    
    print(city_list)
    print(city_dict)
    print(city_typle)
    print(city_set)

def add():
    global city_lis
    global city_dict
    global city_tuple
    global city_set
    gorod = input('Введите название города: ')
    
    city_list.append(gorod)
    city_dict[gorod] = 'Город'
    city_set.add(gorod)
    
    sort()

def delete():
    gorod = input('Введите название города: ')
    global city_lis
    global city_dict
    global city_tuple
    global city_set
    
    del dictionary[slovo]

while True:
    sort()
    menu = """
Выберите действие:
1 - добавление города
3 - удаление города
    """
    vibor = input(menu)
    if vibor == '1':
        add()
    elif vibor == '2':
        delete()
    else:
        print('Неверная команда')
