students = []
for i in range(3):
    print(f"\nВведите данные для студента {i + 1}:")
    name = input("Введите имя студента {i + 1}: ")
    age = int(input("Введите возраст студента {i + 1}: "))
    average_score = float(input("Введите средний балл студента {i + 1}: "))
    group = input("Введите группу студента {i + 1}: ")
   students.append({
        "name": name,
        "age": age,
        "average_score": average_score,
        "group": group
    })
best_student = max(students, key=lambda x: x["average_score"])
print("\nСтудент с самым высоким средним баллом:")
print(f"Введите имя студента {i + 1}: {best_student['name']}, Введите возраст студента {i + 1}: {best_student['age']}, "
      f"Введите средний балл студента {i + 1}: {best_student['average_score']}, Введите группу студента {i + 1}: {best_student['group']}")
average_age = sum(student["age"] for student in students) / len(students)
print(f"\nСредний возраст всех студентов: {average_age:.1f} лет")
groups = [student["group"] for student in students]
has_duplicate_group = len(groups) != len(set(groups)) 
if has_duplicate_group:
    print("\nСреди студентов есть хотя бы два человека из одной группы.")
else:
    print("\nВсе студенты из разных групп.")
