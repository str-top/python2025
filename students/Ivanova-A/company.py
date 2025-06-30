class Employee:
    def calculate_salary(self):
        pass

class Manager(Employee):
    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary
    
    def calculate_salary(self):
        return self.base_salary + (self.base_salary * 0.2)

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
        self.employees.append(employee)
        print(f"Добавлен новый сотрудник: {employee.name}")
    
    def calculate_total_salary(self):
        total = 0
        for emp in self.employees:
            total += emp.calculate_salary()
        return total

my_company = Company()

manager = Manager("Анна Петрова", 100000)
my_company.add_employee(manager)

dev1 = Developer("Иван Сидоров", 160, 1500)
dev2 = Developer("Петр Иванов", 120, 2000)
my_company.add_employee(dev1)
my_company.add_employee(dev2)

total = my_company.calculate_total_salary()
print(f"\nОбщая зарплата всех сотрудников: {total} руб.")

print("\nЗарплаты сотрудников:")
for emp in my_company.employees:
    if isinstance(emp, Manager):
        print(f"Менеджер {emp.name}: {emp.calculate_salary()} руб.")
    else:
        print(f"Разработчик {emp.name}: {emp.calculate_salary()} руб.")
