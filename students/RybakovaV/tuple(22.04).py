people = (('Alice', 30), ('Bob', 25), ('Charlie', 35))

sort = sorted(people, key=lambda x: x[1], reverse=True)
print(sort)
