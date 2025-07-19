import random
import copy

original_list = [1, 2, 3, 4, 5, 6, 7]
current_list = copy.deepcopy(original_list)
shuffles = 0

while True:
    random.shuffle(current_list) 
    shuffles += 1
    if current_list == original_list:  # Сравниваем с исходным
        break

print(f"Список вернулся к исходному порядку после {shuffles} перемешиваний.")
print("Итоговый список:", current_list)
