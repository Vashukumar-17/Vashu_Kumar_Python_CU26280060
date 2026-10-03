# Q20: Find percentage of marks obtained in 5 subjects
max_marks = float(input("Enter maximum marks per subject: "))
total = 0
for subject in range(1, 6):
    total = total + float(input(f"Enter marks of subject {subject}: "))
percentage = (total / (5 * max_marks)) * 100
print(f"Total Marks = {total} / {5 * max_marks}")
print(f"Percentage  = {percentage:.2f}%")
