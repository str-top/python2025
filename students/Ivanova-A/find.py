def find_index(lst, item):
    for i, x in enumerate(lst):
        if x == item:
            return i
    return -1
arr = [5, 2, 8, 2, 9]
print(find_index(arr, 587))
