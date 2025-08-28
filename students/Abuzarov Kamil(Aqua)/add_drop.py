import sqlite3
# Создаем таблицу
conn = sqlite3.connect('lab6.db')
cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS prepodov (
   id INT ,
   FIO TEXT,
   AGE INT,
   id_caf INT,
   id_dolj INT)""")
conn.commit()
 
cur.execute("""CREATE TABLE IF NOT EXISTS doljnost(
    id_dolj INT ,
    nazvanie TEXT
    )""")
 
cur.execute("""CREATE TABLE IF NOT EXISTS cafedra (
   id_caf INT,
   nazvanie TEXT,
   unik TEXT
   )
""")
conn.commit()
 
doljnost = [(1, 'доцент'),(2 ,'аспирант')]
cafedra = [(11, 'ТОРС', 'ПГУТИ'),(12 , 'ПОУТС', 'ПГУТИ')]
prepodov = [(110,'Путовски Игорь Юрьевич', 43,11, 2), (111,'Путовски Валерий Юрьевич', 45, 12, 1), (112, 'Архимедов Рустам Пифагорович', 999, 11, 1)]
conn.commit()
 
cur.executemany("INSERT INTO doljnost VALUES(?,?)", doljnost)
cur.executemany("INSERT INTO cafedra VALUES(?,?,?)", cafedra)
cur.executemany("INSERT INTO prepodov VALUES(?,?,?,?,?)", prepodov)
 
a = """SELECT FIO, doljnost.nazvanie, cafedra.nazvanie  FROM prepodov 
JOIN doljnost 
JOIN cafedra
ON prepodov.id_dolj = doljnost.id_dolj and prepodov.id_caf = cafedra.id_caf"""
 
cur.execute(a)
sql = cur.fetchall()
print(sql)
 
b = """SELECT id_caf, COUNT(*) FROM prepodov GROUP BY id_caf"""
cur.execute(b)
sql1 = cur.fetchall()
print(sql1)
