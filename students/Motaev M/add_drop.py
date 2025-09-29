import sqlite3
import random
import os

db_filename = "library.db"

if os.path.exists(db_filename):
    os.remove(db_filename)
    print(f"Файл базы данных '{db_filename}' удалён.")

conn = sqlite3.connect(db_filename)
cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS readers")
cur.execute("DROP TABLE IF EXISTS books")
conn.commit()
print("Таблицы удалены (если были).")

cur.execute("""
CREATE TABLE books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author TEXT NOT NULL
)
""")

cur.execute("""
CREATE TABLE readers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    book_id INTEGER,
    FOREIGN KEY(book_id) REFERENCES books(id)
)
""")


books = [
    ("1984", "George Orwell"),
    ("The Hobbit", "J.R.R. Tolkien"),
    ("Fahrenheit 451", "Ray Bradbury"),
    ("Dune", "Frank Herbert"),
    ("The Catcher in the Rye", "J.D. Salinger"),
]
cur.executemany("INSERT INTO books (title, author) VALUES (?, ?)", books)

names = ["Anna", "Boris", "Clara", "David", "Elena", "Fedor", "Galina", "Igor"]
for _ in range(20):
    name = random.choice(names)
    age = random.randint(15, 60)
    book_id = random.randint(1, len(books))
    cur.execute("INSERT INTO readers (name, age, book_id) VALUES (?, ?, ?)",
                (name, age, book_id))

conn.commit()
print("Данные добавлены.")

print("\nСредний возраст читателей:")
for row in cur.execute("SELECT AVG(age) FROM readers"):
    print(round(row[0], 1))

print("\nСколько читателей у каждой книги:")
for row in cur.execute("""
SELECT books.title, COUNT(readers.id)
FROM books
LEFT JOIN readers ON books.id = readers.book_id
GROUP BY books.id
"""):
    print(row)

print("\nКнига с наибольшим числом читателей:")
for row in cur.execute("""
SELECT books.title, COUNT(readers.id) as cnt
FROM books
LEFT JOIN readers ON books.id = readers.book_id
GROUP BY books.id
ORDER BY cnt DESC
LIMIT 1
"""):
    print(row)

cur.execute("DELETE FROM readers")
cur.execute("DELETE FROM books")
conn.commit()
print("\nВсе данные из таблиц удалены.")

cur.execute("DROP TABLE readers")
cur.execute("DROP TABLE books")
conn.commit()
print("Таблицы удалены.")

conn.close()

if os.path.exists(db_filename):
    os.remove(db_filename)
    print(f"Файл базы данных '{db_filename}' удалён в конце скрипта.")
