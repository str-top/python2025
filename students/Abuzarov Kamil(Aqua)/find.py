def find(my_list, value):
    index = 0;
    for element in my_list:
        if element == value:
            return index
        index += 1
    return -1
