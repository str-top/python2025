1,John Doe,85,95%
2,Jane Smith,92,88%
ID,Name,Grade,Attendance

students = [
    {"id": 1, "name": "Alice", "grade": 90},
    {"id": 2, "name": "Bob", "grade": 75}
]


import pandas as pd
df = pd.DataFrame(students)
print(df["grade"].mean())  # Average grade


CREATE TABLE students (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    grade INT,
    email VARCHAR(100)
);


import matplotlib.pyplot as plt
plt.bar(df["name"], df["grade"])
plt.show()
