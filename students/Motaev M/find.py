def find_first_index(lst, target):

    for index, value in enumerate(lst):
        if value == target:
            return index
    return -1

my_list = [5, 3, 7, 3, 9, 10]
target_element = 3

result = find_first_index(my_list, target_element)
print(f"Индекс первого вхождения элемента {target_element}: {result}") 
