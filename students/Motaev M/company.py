from abc import ABC, abstractmethod
class Employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass

class Manager(Employee):
    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary

    def calculate_salary(self):
        return self.base_salary * 1.20

    def __str__(self):
        return f"Менеджер: {self.name}, Зарплата: {self.calculate_salary()}"

class Developer(Employee):
    def __init__(self, name, hours_worked, hourly_rate):
        self.name = name
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate

    def calculate_salary(self):
        return self.hours_worked * self.hourly_rate

    def __str__(self):
        return f"Разработчик: {self.name}, Зарплата: {self.calculate_salary()}"

class Company:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def calculate_total_salary(self):
        total_salary = 0
        for employee in self.employees:
            total_salary += employee.calculate_salary()
        return total_salary

    def display_employees(self):
        if not self.employees:
            print("В компании нет сотрудников.")
        else:
            print("Сотрудники компании:")
            for employee in self.employees:
                print(employee)
              
company = Company()

manager1 = Manager("Alice", 50000)
developer1 = Developer("Bob", 160, 250)
developer2 = Developer("Charlie", 180, 200)
company.add_employee(manager1)
company.add_employee(developer1)
company.add_employee(developer2)
total_salary = company.calculate_total_salary()
print(f"Общая сумма зарплат: {total_salary}")
company.display_employees()
