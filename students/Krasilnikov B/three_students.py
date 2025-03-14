# TASK1


students = []

for i in range(1,4):
    student = ()
    student_list = list(student)
    student_list.append(input(f"Введите имя студента {i} "))
    student_list.append(int(input(f"Введите возраст студента {i} ")))
    student_list.append(float(input(f"Введите средний балл студента {i} ")))
    student_list.append(input(f"Введите группу студента {i} "))
    student = tuple(student_list)
    students.append(student)

# TASK2
top_student = max(students, key=lambda x: x[2])

print("Студент с самой высокой средней оценкой: ")
print(f"Имя: {top_student[0]}, Возраст: {top_student[1]}, Средний балл: {top_student[2]}, Группа: {top_student[3]}")
# TASK3
sum_age = 0
for age in students:
    sum_age += age[1]
middle_age = sum_age / len(students)
print(f'Средний возраст всех студентов: {middle_age}')

# TASK3
group_list = {}
for student in students:
    group = student[3]
    if group in group_list:
        group_list[group] += 1
    else:
        group_list[group] = 1

for group, count in group_list.items():
    if count >=2:
        print(f'в этом списке есть {count} человека из группы {group}')
        break
    else:
        print('в этом списке нет одногруппников')




