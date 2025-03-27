[
    {'name': 'Иван', 'age': 20, 'average_score': 4.5, 'group': 'A'},
    {'name': 'Мария', 'age': 21, 'average_score': 4.8, 'group': 'B'},
    {'name': 'Алексей', 'age': 19, 'average_score': 4.2, 'group': 'A'}
]

Шаг 2: Поиск студента с самым высоким баллом

best_student = max(students, key=lambda x: x['average_score'])
print("\nСтудент с самым высоким средним баллом:")
print(f"Имя: {best_student['name']}, Возраст: {best_student['age']}, "
      f"Средний балл: {best_student['average_score']}, Группа: {best_student['group']}")

Шаг 3: Расчет среднего возраста

average_age = sum(student['age'] for student in students) / len(students)
print(f"\nСредний возраст всех студентов: {average_age:.1f} лет")

Шаг 4: Проверка студентов из одной группы

groups = [student['group'] for student in students]
has_duplicate_group = len(groups) != len(set(groups))

if has_duplicate_group:
    print("\nЕсть студенты из одной группы.")
else:
    print("\nВсе студенты из разных групп."

2) задание 

[
    {'name': 'Анна', 'age': 20, 'average_score': 4.7, 'group': 'B'},
    {'name': 'Петр', 'age': 21, 'average_score': 4.9, 'group': 'A'},
    {'name': 'Мария', 'age': 19, 'average_score': 4.5, 'group': 'B'}
]

1.Расчет среднего возраста:

sum(student['age'] for student in students)  # Аналог цикла for


2.Проверка групп:

groups = [student['group'] for student in students]  # Создание списка групп

4. Как можно изменить цикл for?
Вариант 1: Сделать количество студентов переменным.

n = int(input("Сколько студентов? "))
for i in range(1, n + 1):  # Для n студентов
    ...

Вариант 2: Использовать enumerate для красивого вывода.


for idx, _ in enumerate(students, 1):  # idx = 1, 2, 3
    print(f"\nВведите данные студента {idx}:")
