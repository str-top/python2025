people = (('Alice', 30), ('Bob', 25), ('Charlie', 35))

# Сортируем по возрасту (второй элемент кортежа) в порядке убывания
sorted_people = tuple(sorted(people, key=lambda x: x[1], reverse=True))

print(sorted_people)

(('Charlie', 35), ('Alice', 30), ('Bob', 25))
