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
        
class Developer(Employee):
    def __init__(self, name, hours_worked, hourly_rate):
        self.name = name
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate
    def calculate_salary(self):
        return hours_worked * hourly_rate
        
class Company:
    def __init__(self):
        employees = []
    def add_employee(employee):
        self.employees.append(employee)
    def calculate_total_salary():
        total_salary = 0
        for employee in self.employees:
            total_salary += employee.calculate_salary()
        return total_salary
manager = Manager("Иван Иванов", 50000)
developer = Developer("Петр Петров", 160, 1500)
      
manager.calculate_salary()    

developer.calculate_salary()    

company = Company()
company.add_employee(developer)
company.add_employee(manager)
company.get_info()
company.calculate_total_salary()
print(f"Общая зарплата всех сотрудников: {company.calculate_total_salary():.2f} руб.")
