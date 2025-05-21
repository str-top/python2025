def find_first_index(lst, target):
    for index in range(len(lst)):
        if lst[index] == target:
            return index
    return -1

numbers = [10, 20, 30, 40, 50]
print(find_first_index(numbers, 30))  
print(find_first_index(numbers, 77))  
