# Q21. Create student.txt and write five student records using write().

records = [
    "101,Amit,78.5\n",
    "102,Priya,91.0\n",
    "103,Ravi,84.0\n",
    "104,Neha,88.5\n",
    "105,Karan,76.0\n",
]

with open("student.txt", "w", encoding="utf-8") as file:
    for record in records:
        file.write(record)

print("Five student records written to student.txt.")
