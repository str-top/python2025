
def get_student_info(student_number):
    name = input(f"Введите имя студента {student_number}: ")
    age = int(input(f"Введите возраст студента {student_number}: "))
    average_grade = float(input(f"Введите средний балл студента {student_number}: "))
    group = input(f"Введите группу студента {student_number}: ")
    return {
        'name': name,
        'age': age,
        'average_grade': average_grade,
        'group': group
    }


students = []


for i in range(1, 4):
    student_info = get_student_info(i)
    students.append(student_info)

top_student = max(students, key=lambda student: student['average_grade'])

average_age = sum(student['age'] for student in students) / len(students)

group_count = {}
for student in students:
    group = student['group']
    if group in group_count:
        group_count[group] += 1
    else:
        group_count[group] = 1

same_group = any(count >= 2 for count in group_count.values())

print(f"\nСтудент с самым высоким баллом: {top_student['name']}, {top_student['age']} лет, группа {top_student['group']}, балл {top_student['average_grade']}")
print(f"Средний возраст студентов: {average_age:.1f} лет")
print(f"Есть студенты из одной группы: {'Да' if same_group else 'Нет'}")
несамделал/(
