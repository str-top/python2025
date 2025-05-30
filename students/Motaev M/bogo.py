import random
def bogosort(spisok):
    sorted_spisok = list(spisok)

    def is_sorted(l):
        for i in range(len(l) - 1):
            if l[i] > l[i+1]:
                return False
        return True

    while not is_sorted(sorted_spisok):
        random.shuffle(sorted_spisok)
    
    return sorted_spisok
    
numbers = [3, 1, 2, 5, 4]

sorted_numbers = bogosort(numbers)

print("Исходный список:", numbers)
print("Отсортированный список:", sorted_numbers)
