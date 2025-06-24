def find_best_student(students_list):
    """Находит студента с самым высоким средним баллом"""
    best = students_list[0]  # начинаем с первого студента
    for student in students_list:
        if student['average_score'] > best['average_score']:
            best = student
    return best

students = []
for i in range(1, 4):
    print(f"\nВведите данные студента {i}:")
    name = input("Имя: ")
    age = int(input("Возраст: "))
    average_score = float(input("Средний балл: "))
    group = input("Группа: ")
    students.append({
        'name': name,
        'age': age,
        'average_score': average_score,
        'group': group
    })

best_student = find_best_student(students)
print("\nСтудент с самым высоким средним баллом:")
print(f"Имя: {best_student['name']}")
print(f"Возраст: {best_student['age']}")
print(f"Средний балл: {best_student['average_score']}")
print(f"Группа: {best_student['group']}")

average_age = sum(student['age'] for student in students) / len(students)
print(f"\nСредний возраст всех студентов: {average_age:.1f}")


same_group = False

if students[0]['group'] == students[1]['group']:
    same_group = True
elif students[0]['group'] == students[2]['group']:
    same_group = True
elif students[1]['group'] == students[2]['group']:
    same_group = True

if same_group:
    print("\nЕсть студенты из одной группы.")
else:
    print("\nВсе студенты из разных групп.")
