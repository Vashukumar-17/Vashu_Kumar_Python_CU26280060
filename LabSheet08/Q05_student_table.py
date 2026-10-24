# Q5. Print student details in an aligned table.

name = input("Enter student name: ")
roll = input("Enter roll number: ")
percentage = float(input("Enter percentage: "))

print("-" * 48)
print(f"{'Name':<20}{'Roll Number':<15}{'Percentage':>13}")
print("-" * 48)
print(f"{name:<20}{roll:<15}{percentage:>12.2f}%")
print("-" * 48)
