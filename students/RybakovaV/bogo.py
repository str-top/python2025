import random
import time
def bogosort(lst):
    """
    Сортирует список методом BogoSort.
    Алгоритм:
    1. Проверяет, отсортирован ли список
    2. Если нет - перемешивает случайным образом
    3. Повторяет до тех пор, пока список не отсортируется
    """
    def is_sorted(arr):
        """Проверяет, отсортирован ли список"""
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                return False
        return True
    # Пока список не отсортирован, перемешиваем его
    while not is_sorted(lst):
        random.shuffle(lst)
    
    return lst
test_list = [3, 1, 2, 4]
print("Исходный список:", test_list)
start_time = time.time()
sorted_list = bogosort(test_list.copy())
end_time = time.time()
print("Отсортированный список:", sorted_list)
print(f"Время выполнения: {end_time - start_time:.5f} секунд")
