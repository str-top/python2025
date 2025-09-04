class Student:
    def __init__(self, id, name, group, gpa):
        self.id = id
        self.name = name
        self.group = group
        self.gpa = gpa
class StudentModel:
    def __init__(self):
        self.students = []

    def create(self, student):
        self.students.append(student)

    def read(self,name):
        for student in self.students:
            if student.name == name:
                print(f'id: {student.id}, name: {student.name}, group: {student.group}, gpa: {student.gpa}')
                return student
        return None
        
    def delete(self,name):
        for student in self.students:
            if student.name in student:
                self.students.remove(student)
        return False

class StudentView:
    def show_menu(self):
        choice = input('''
            1. Добавить студента
            2. Удалить студента
            3. Просмотреть всех студентов
            4. Поиск студентов
            5. выход

        ''')
        return choice
    
    def get_student_name(self):
        name = input('Как зовут студента которого мы ищем?')
        return name
        
        
    def get_student_data(self):
        idd = input('Какой id будет у нового студента?')
        name = input('Как зовут нового студента?')
        group = input('В какую группу его?')
        gpa = float(input('И его средний балл'))
        
        return Student(idd, name, group, gpa)

class StudentController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def run(self):
        while True:
            choice = self.view.show_menu()
            
            if choice == '0':
                print('Выход из программы')
            elif choice == '1':
                student = self.view.get_student_data()
                self.model.create(student)
            elif choice == '2':
                student_name = self.view.get_student_name()
                self.model.read(student_name)
            elif choice == '3':
                student_name = self.view.get_student_name()
                self.model.delete(student_name)

if __name__ == "__main__":
    model = StudentModel()
    view = StudentView()
    controller = StudentController(model, view)
    controller.run()

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
