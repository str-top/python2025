# Programma dlya rascheta zarplaty sotrudnikov s uchetom bonusov i vychetov

employees = {
    "Ivan": {"base_salary": 50000, "bonus": 5000, "deductions": 3000},
    "Marina": {"base_salary": 55000, "bonus": 7000, "deductions": 2000},
    "Maksim": {"base_salary": 45000, "bonus": 3000, "deductions": 1500},
    "Olga": {"base_salary": 60000, "bonus": 8000, "deductions": 4000},
}

min_salary = 50000  # Minimalnaya zarplata dlya polucheniya bonusa
max_deductions = 3000  # Maksimalnyy razmer vychetov dlya polucheniya bonusa
total_expense = 0  # Obshchie raskhody kompanii na zarplatu
high_salary_employees = []  # Spisok sotrudnikov s vysokoy zarplatoy

# Protsess rascheta zarplaty
print(employees)
print(employees.items())

for name, data in employees.items():
    base_salary = data["base_salary"]
    bonus = data["bonus"]
    deductions = data["deductions"]

    # Esli vychety bolshe, chem maksimalnyy limit, ne daem bonus
    if deductions > max_deductions:
        print(f"{name} ne poluchaet bonus iz-za vysokikh vychetov.")
        continue  # Propuskaem etogo sotrudnika

    total_salary = base_salary + bonus - deductions
    total_expense += total_salary

    # Proverka dlya dobavleniya v spisok sotrudnikov s vysokoy zarplatoy
    if total_salary > min_salary:
        high_salary_employees.append(name)

    print(f"{name}: Okonchatelnaya zarplata = {total_salary}")

# Vyvod itogovykh rezul'tatov
while True:
    if high_salary_employees:
        print(f"\nSotrudniki s vysokoy zarplatoy (bolshe {min_salary}): {', '.join(high_salary_employees)}")
    else:
        print("\nNet sotrudnikov s vysokoy zarplatoy.")
    break  # Zavershaem tsikl posle vyvoda

print(f"\nObshchie raskhody kompanii na zarplaty: {total_expense}")
