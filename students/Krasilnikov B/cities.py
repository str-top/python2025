city_list = ['Москва']
city_dict = {'Москва':'Столица'}
city_tuple = ('Москва')
city_set = {'Москва'}


def sort():
    global city_list
    global city_dict
    global city_tuple
    global city_set
    
    city_list = sorted(city_list, key=lambda x: len(x))
    city_dict = sorted(city_list, key=lambda x: len(x[0]))
    
    print(city_list)
    print(city_dict)
    print(city_tuple)
    print(city_set)
    
def add():
    global city_list
    global city_dict
    global city_tuple
    global city_set
    
    gorod = input ('ВВедите название города')
    city_list.append(gorod)
    city_dict[gorod]= 'город'
    city_set.add(gorod)
    sort()
    
def del():
    pass


while True:
    menu = ''' 
    Выберите действие:
    1 - добавление города
    2 - удаление города
    
    '''
    vibor = input('ВВедите 1 или 2')
    if vibor == '1':
        add()
    elif vibor == '2':
        del()
    else:
        print('Неверная команда')
