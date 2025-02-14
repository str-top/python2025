# 1. Подсчет количества коробок
box_count = 0
total_boxes = 10  # Общее количество коробок для подсчета

while box_count < total_boxes:
    box_count += 1
    print(f"Подсчитано коробок: {box_count}")

print("Все коробки подсчитаны!\n")

# 2. Ожидание заморозки фарша в морозильнике
import time

freezing_time = 30  # Время заморозки в секундах
current_time = 0

while current_time < freezing_time:
    print(f"Ожидание заморозки... Прошло {current_time} секунд")
    time.sleep(1)  # Ожидание 1 секунду
    current_time += 1

print("Фарш заморожен!\n")

# 3. Условно-бесконечный цикл
while True:
    user_input = input("Введите 'стоп' для выхода из цикла: ")
    if user_input.lower() == 'стоп':
        print("Цикл остановлен.")
        break
    else:
        print("Продолжаем цикл...")
