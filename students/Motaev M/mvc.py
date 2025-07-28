import sys
class Student:
    _id_counter = 1

    def __init__(self, name: str, group: str, gpa: float):
        self.id = Student._id_counter
        Student._id_counter += 1
        self.name = name
        self.group = group
        self.gpa = gpa

    def __str__(self):
        return f"ID: {self.id}, ФИО: {self.name}, Группа: {self.group}, Средний балл: {self.gpa}"

class StudentModel:
    def __init__(self):
        self.students = []

    def add_student(self, name: str, group: str, gpa: float):
        student = Student(name, group, gpa)
        self.students.append(student)
        return student

    def delete_student(self, student_id: int):
        for i, student in enumerate(self.students):
            if student.id == student_id:
                del self.students[i]
                return True
        return False

    def get_all_students(self):
        return self.students

    def find_student_by_id(self, student_id: int):
        for student in self.students:
            if student.id == student_id:
                return student
        return None
      
def display_menu():
    print("\n=== Меню ===")
    print("1. Добавить студента")
    print("2. Удалить студента по ID")
    print("3. Показать всех студентов")
    print("4. Выйти")

def display_students(students):
    if not students:
        print("Список студентов пуст.")
    else:
        print("\nСписок студентов:")
        for student in students:
            print(student)

def get_student_input():
    name = input("Введите ФИО: ")
    group = input("Введите номер группы: ")
    while True:
        try:
            gpa = float(input("Введите средний балл: "))
            break
        except ValueError:
            print("Некорректный ввод. Попробуйте снова.")
    return name, group, gpa

def get_student_id():
    while True:
        try:
            student_id = int(input("Введите ID студента: "))
            return student_id
        except ValueError:
            print("Некорректный ввод. Попробуйте снова.")

class StudentController:
    def __init__(self, model):
        self.model = model

    def add_student(self):
        name, group, gpa = get_student_input()
        student = self.model.add_student(name, group, gpa)
        print(f"Студент добавлен с ID {student.id}.")

    def delete_student(self):
        student_id = get_student_id()
        success = self.model.delete_student(student_id)
        if success:
            print(f"Студент с ID {student_id} удален.")
        else:
            print(f"Студент с ID {student_id} не найден.")

    def show_all_students(self):
        students = self.model.get_all_students()
        display_students(students)

def main():
    model = StudentModel()
    controller = StudentController(model)

    while True:
        display_menu()
        choice = input("Выберите дaействие (1-4): ")

        if choice == '1':
            controller.add_student()
        elif choice == '2':
            controller.delete_student()
        elif choice == '3':
            controller.show_all_students()
        elif choice == '4':
            print("Выход из программы.")
            sys.exit()
        else:
            print("Некорректный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()
