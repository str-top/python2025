people = (('Alice', 30), ('Bob', 25), ('Charlie', 35))
age = sorted(people, key=lambda x: x[1], reverse = True)
print(age)
