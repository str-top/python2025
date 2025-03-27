# Ввод данных о трех студентах
students = []
for i in range(1, 4):
    print(f"\nВведите данные студента {i}:")
    name = input("Имя: ")
    age = int(input("Возраст: "))
    average_score = float(input("Средний балл: "))
    group = input("Группа: ")
    
    student = {
        'name': name,
        'age': age,
        'average_score': average_score,
        'group': group
    }
    students.append(student)

# 1. Определение студента с самым высоким средним баллом
best_student = max(students, key=lambda x: x['average_score'])
print("\nСтудент с самым высоким средним баллом:")
print(f"Имя: {best_student['name']}, Возраст: {best_student['age']}, "
      f"Средний балл: {best_student['average_score']}, Группа: {best_student['group']}")

# 2. Вычисление среднего возраста всех студентов
average_age = sum(student['age'] for student in students) / len(students)
print(f"\nСредний возраст всех студентов: {average_age:.1f} лет")

# 3. Проверка, есть ли хотя бы два студента из одной группы
groups = [student['group'] for student in students]
has_duplicate_group = len(groups) != len(set(groups))

if has_duplicate_group:
    print("\nЕсть студенты из одной группы.")
else:
    print("\nВсе студенты из разных групп.")
