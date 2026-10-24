# Q16. Find student with the highest marks.

students = {"Amit": 78, "Priya": 91, "Ravi": 84, "Neha": 91}

if not students:
    print("No student records available.")
else:
    top_name = None
    top_marks = None
    for name, marks in students.items():
        if top_marks is None or marks > top_marks:
            top_name = name
            top_marks = marks

    print("Highest marks:", top_marks)
    print("Student:", top_name)
    print("All top scorers:", [name for name, marks in students.items() if marks == top_marks])
