import random

listo = [1,2,3,4,5,6,7,8,9]
# попробуйте с шафлом и без него проверить
# random.shuffle(listo)
def bogosort(lst):
    while True:
        is_sort = True
        for i in range(len(lst) - 1):
            if lst[i] > lst[i + 1]:
                print(lst)
                print('ошибка')
                is_sort = False
                
                break

                
        if is_sort:
            print(f'список отсортирован: {lst}')
            break
        random.shuffle(lst)
bogosort(listo)
