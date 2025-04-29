people = (('Alice', 30), ('Bob', 25), ('Charlie', 35))
sortirovka = sorted(people, key=lambda x: x[1], reverse=True)
sortirovka = tuple(sortirovka)
print(sortirovka)
