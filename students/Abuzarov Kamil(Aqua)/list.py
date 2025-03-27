from collections import OrderedDict

numbers = [10, 2, 5, 4, 5, 6, 9, 7, 9, 1, 3, 8]
unique_numbers = list(OrderedDict.fromkeys(numbers))  # Удаляет дубликаты, сохраняя порядок
sorted_numbers = sorted(unique_numbers, reverse=True)

print(sorted_numbers)  # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
