new_list = [1,7,2,66,3,9,7]
print(f'Есть следующий список: \n {new_list}')


def question():
    answer = int(input(f'''
    Что будем делать?
    0 = добавим элемент в конец,
    1 = удалим элемент если он повторяется,
    2 = поищем индекс элемента
    3 = отсортируем список
    4 = перевернем список
    (принимаются только цифры)
    '''))
    return answer



def zero():
    add = int(input('Что будем добавлять в список?'))
    new_list.append(add)
    print(f'Итог таков: \n {new_list}')



def one():
    again_elem = 0
    add = int(input('Что будем удалять из списока?'))
    for i in range(len(new_list)):
        for j in range(i+1,len(new_list)):
            if new_list[i] == new_list[j]:
                again_elem = new_list[i]
                
    if add != again_elem:
        print(f'Данный элемент не повторяется в этом списке \n {new_list}')
        one()
    else:
        new_list.remove(add)
    print(f'Итог таков: \n {new_list}')
    
def two():
    search = int(input('Индекс какого элемента будем искать?'))
    search_index = new_list.index(search)
    print(f'Итог таков: \n {search_index}')
    
def three():
    new_list.sort()
    print(f'Итог таков: \n {new_list}')
    
def four():
    new_list.reverse()
    print(f'Итог таков: \n {new_list}')
    
    
    
x = 0

while x < 5:
    answer = question()

    if answer == 0:
        print('Выбрант вариант "0"')
        zero()
        x += 1
        
    elif answer == 1:
        print('Выбрант вариант "1"')
        one()
        x += 1
    
    elif answer == 2:
        print('Выбрант вариант "2"')
        two()
        x += 1
    
    elif answer == 3:
        print('Выбрант вариант "3"')
        three()
        x += 1
    
    elif answer == 4:
        print('Выбрант вариант "4"')
        four()
        x += 1
    
            








        
    
