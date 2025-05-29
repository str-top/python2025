from abc import ABC, abstractmethod

class Employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass


class Manager(Employee):
    employee = []
    def __init__(self,name,base_salary):
        self.name = name
        self.base_salary = base_salary
        
    def calculate_salary(self):
        return self.base_salary + (self.base_salary / 100 * 20)
        
    def get_info(self):
        self.employee.append(self.name)
        self.employee.append(self.calculate_salary())
        print(self.employee)
        
        
        
class Developer(Employee):
    employee = []
    def __init__(self,name,hours_worked,hourly_rate):
        self.name = name
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate
        
    def calculate_salary(self):
        return self.hours_worked * self.hourly_rate
        
    def get_info(self):
        self.employee.append(self.name)
        self.employee.append(self.calculate_salary())
        print(self.employee)
        return self.employee
        
        
        
class Company:
    employees = []
        
    def add_employee(self,employee):
        self.employees.append(employee)
        
    def calculate_total_salary(self):
        total_salary = 0
        for employee in self.employees:
            total_salary += employee.calculate_salary()
        print(total_salary)
    
    def get_info(self):
        for employee in self.employees:
            print(employee.name)
            
        
        
developer = Developer('Akakiy',500, 160)
manager = Manager('Farida',42500)
        
developer.calculate_salary()        
developer.get_info()        
        
manager.calculate_salary()        
manager.get_info()        
        
        
        
company = Company()
company.add_employee(developer)
company.add_employee(manager)
company.get_info()
company.calculate_total_salary()

        
        
        
        
