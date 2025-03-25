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

best_student = max(students, key=lambda x: x['average_score'])
print("\nСтудент с самым высоким средним баллом:")
print(f"Имя: {best_student['name']}, Возраст: {best_student['age']}, "
      f"Средний балл: {best_student['average_score']}, Группа: {best_student['group']}")

average_age = sum(student['age'] for student in students) / len(students)
print(f"\nСредний возраст студентов: {average_age:.1f} лет")

groups = [student['group'] for student in students]
has_same_group = len(groups) != len(set(groups))

if has_same_group:
    print("\nЕсть студенты из одной группы!")
else:
    print("\nВсе студенты из разных групп.")

print("\nВсе студенты:")
for student in students:
    print(f"{student['name']} ({student['group']}) - {student['age']} лет, балл: {student['average_score']}")
