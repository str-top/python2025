city_list = ['Москва', 'Питер']
city_dict = {'Москва' : 'Столица', 'Питер' : 'Культурная столица'}
city_tuple = ('Москва')
city_set = {'Москва'}

def sort():
    global city_list
    global city_dict
    global city_tuple
    global city_set
    
    city_list = sorted(city_list, key=lambda x: len(x))
    # city_dict = sorted(city_dict, key=lambda x: len(x[0]))
    
    print(city_list)
    print(city_dict)
    print(city_tuple)
    print(city_set)
    
def add():
    global city_list
    global city_dict
    global city_tuple
    global city_set
    gorod = input('Введите название города')
    
    city_list.append(gorod)
    city_dict[gorod] = 'город'
    city_set.add(gorod)
    
    sort()
    
def delete():
    global city_list
    global city_dict
    global city_tuple
    global city_set
    
while True:
    sort()
    menu = """
    Выберите действие:
    1 - добавление слова
    2 - вывод значения слова
    """
     vibor = input(menu)
    if vibor == '1':
        add()
    elif vibor == '2':
        delete()
    else:
        print('неверная команда')
