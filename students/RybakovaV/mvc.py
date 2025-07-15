class Student:
    def __init__(self, id, name, group, gpa):
        self.id = id
        self.name = name
        self.group = group
        self.gpa = gpa

    def __str__(self):
        return f"ID: {self.id}, имя: {self.name}, группа: {self.group}, средний балл: {self.gpa}"


class StudentModel:
    def __init__(self):
        self.students = []
        self.next_id = 1

    def add_student(self, name, group, gpa):
        student = Student(self.next_id, name, group, gpa)
        self.students.append(student)
        self.next_id += 1
        return student

    def get_all_students(self):
        return self.students.copy()

    def get_student_by_id(self, id):
        for student in self.students:
            if student.id == id:
                return student
        return None

    def delete_student(self, id):
        student = self.get_student_by_id(id)
        if student:
            self.students.remove(student)
            return True
        return False

    def search_students(self, keyword):
        keyword = keyword.lower()
        return [student for student in self.students 
                if keyword in student.name.lower() 
                or keyword in student.group.lower()]
                
class StudentView:
    @staticmethod
    def display_menu():
        print("\nСистема управления студентами")
        print("1. Добавить студента")
        print("2. Удалить студента")
        print("3. Просмотреть всех студентов")
        print("4. Поиск студентов")
        print("5. выход")

    @staticmethod
    def get_input(prompt):
        return input(prompt)

    @staticmethod
    def display_message(message):
        print(message)

    @staticmethod
    def display_students(students):
        if not students:
            print("Студент не найден.")
        else:
            print("\nСписок студентов:")
            for student in students:
                print(student)

    @staticmethod
    def get_student_details():
        name = input("Введите имя студента: ")
        group = input("Введите номер группы: ")
        while True:
            try:
                gpa = float(input("введите средний балл: "))
                if 0 <= gpa <= 5:
                    break
                print("Средний балл должен быть от 0 до 5")
            except ValueError:
                print("Пожалуйста, введите правильный номер для GPA")
        return name, group, gpa

    @staticmethod
    def get_student_id():
        while True:
            try:
                return int(input("введите ID студента: "))
            except ValueError:
                print("Пожалуйста, введите корректное целое число для ID")
                

class StudentController:
    def __init__(self):
        self.model = StudentModel()
        self.view = StudentView()

    def run(self):
        while True:
            self.view.display_menu()
            choice = self.view.get_input("Введите свой выбор (1–5): ")

            if choice == '1':
                self.add_student()
            elif choice == '2':
                self.delete_student()
            elif choice == '3':
                self.view_all_students()
            elif choice == '4':
                self.search_students()
            elif choice == '5':
                self.view.display_message("Завершение работы программы. До свидания!")
                break
            else:
                self.view.display_message("Неверный выбор. Пожалуйста, попробуйте ещё раз.")

    def add_student(self):
        name, group, gpa = self.view.get_student_details()
        student = self.model.add_student(name, group, gpa)
        self.view.display_message(f"Студент успешно добавлен с ID: {student.id}")

    def delete_student(self):
        student_id = self.view.get_student_id()
        if self.model.delete_student(student_id):
            self.view.display_message(f"Студент с удостоверением личности {student_id} успешно удален")
        else:
            self.view.display_message(f"Студент с удостоверением личности {student_id} не найдено")

    def view_all_students(self):
        students = self.model.get_all_students()
        self.view.display_students(students)

    def search_students(self):
        keyword = self.view.get_input("Введите ключевое слово для поиска (имя или группу): ")
        students = self.model.search_students(keyword)
        self.view.display_students(students)

if __name__ == "__main__":
    app = StudentController()
    app.run()
