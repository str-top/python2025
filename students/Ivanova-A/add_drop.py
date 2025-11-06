import sqlite3
import random
import os

# --- Задание 1: создание структуры базы ---
conn = sqlite3.connect("library.db")
cur = conn.cursor()

# Удаление таблиц если они существуют
cur.execute("DROP TABLE IF EXISTS readers")
cur.execute("DROP TABLE IF EXISTS books")

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

# --- Задание 2: заполнение базы случайными данными ---
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
    book_id = random.randint(1, len(books))  # читатель берет книгу
    cur.execute("INSERT INTO readers (name, age, book_id) VALUES (?, ?, ?)",
                (name, age, book_id))

conn.commit()

# --- Задание 3: чтение и вычисления ---
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

print("\n--- Удаление данных ---")

print("\nУдаляем читателей младше 20 лет:")
cur.execute("DELETE FROM readers WHERE age < 20")
conn.commit()
print(f"Удалено записей: {cur.rowcount}")

print("\nУдаляем всех читателей:")
cur.execute("DELETE FROM readers")
conn.commit()
print(f"Удалено всех читателей: {cur.rowcount}")

print("\nПытаемся удалить книги (ожидаем ошибку внешнего ключа):")
try:
    cur.execute("DELETE FROM books")
    conn.commit()
    print("Книги удалены")
except sqlite3.IntegrityError as e:
    print(f"Ошибка при удалении книг: {e}")

print("\nУдаляем таблицы:")
cur.execute("DROP TABLE IF EXISTS readers")
cur.execute("DROP TABLE IF EXISTS books")
print("Таблицы удалены")

conn.close()

print("\nУдаляем файл базы данных:")
if os.path.exists("library.db"):
    os.remove("library.db")
    print("Файл library.db удален")
else:
    print("Файл library.db не существует")я
