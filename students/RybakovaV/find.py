def find_index(lst, target):
    """
    Возвращает индекс первого вхождения элемента в списке или -1, если элемент не найден.
    
    :param lst: список для поиска
    :param target: искомый элемент
    :return: индекс элемента или -1
    """
    for index, value in enumerate(lst):
        if value == target:
            return index
    return -1
numbers = [5, 3, 8, 2, 9, 3, 7]
print(find_index(numbers, 3))  # 1 (первое вхождение 3)
print(find_index(numbers, 7))  # 6
print(find_index(numbers, 4))  # -1 (не найдено)
