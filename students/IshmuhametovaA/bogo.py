import random

def is_sorted(lst):
    return all(lst[i] <= lst[i + 1] for i in range(len(lst) - 1))

def bogosort(lst):
    """Сортирует список с помощью алгоритма bogosort."""
    while not is_sorted(lst):
        random.shuffle(lst) 
    return lst

if __name__ == "__main__":
    numbers = [77, 444, 42, 11, 47]
    sorted_numbers = bogosort(numbers)
    print("Отсортированный список:", sorted_numbers)
