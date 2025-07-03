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
        return self.base_salary * 1.2

class Developer(Employee):
    def __init__(self, name, hours_worked, hourly_rate):
        self.name = name
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate

    def calculate_salary(self):
        return self.hours_worked * self.hourly_rate

class Company:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        if isinstance(employee, Employee):
            self.employees.append(employee)
        else:
            raise TypeError("объект должен быть наследственным от класса Employee или его подкласса.")

    def calculate_total_salary(self):
        total = 0
        for employee in self.employees:
            total += employee.calculate_salary()
        return total

if __name__ == "__main__":
    company = Company()

    manager1 = Manager("Иван Иванов", 5000)
    developer1 = Developer("Петр Петров", 160, 25)
    developer2 = Developer("Светлана Смирнова", 120, 30)

    company.add_employee(manager1)
    company.add_employee(developer1)
    company.add_employee(developer2)

    print(f"Общая сумма зарплат: {company.calculate_total_salary():.2f}")
