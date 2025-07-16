# model.py
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

# view.py
class StudentView:
    def show_menu(self):
        choice = input('''
            1 - добавить студента
            2 - найти студента
            3 - удалить студента
            0 - выйти
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

# controller.py
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

# main.py
if __name__ == "__main__":
    model = StudentModel()
    view = StudentView()
    controller = StudentController(model, view)
    controller.run()
