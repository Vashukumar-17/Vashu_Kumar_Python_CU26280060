# Q23. Append three records without deleting existing contents.

new_records = [
    "106,Meera,89.0\n",
    "107,Arjun,82.5\n",
    "108,Simran,94.0\n",
]

with open("student.txt", "a", encoding="utf-8") as file:
    for record in new_records:
        file.write(record)

print("Three records appended to student.txt.")
