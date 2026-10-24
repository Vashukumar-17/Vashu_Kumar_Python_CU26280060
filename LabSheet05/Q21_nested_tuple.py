# Q21: Create a nested tuple and access its elements

# A nested tuple: each inner tuple holds (roll number, name, marks)
students = (
    (101, "Aman", 85),
    (102, "Riya", 92),
    (103, "Karan", 78),
)

print("Nested tuple:", students)

# Access using double indexing: tuple[outer][inner]
print("\nFirst student        :", students[0])
print("Name of 2nd student  :", students[1][1])
print("Marks of 3rd student :", students[2][2])

# Access using user-supplied indexes
outer = int(input("\nEnter outer index (0-2): "))
inner = int(input("Enter inner index (0-2): "))
if 0 <= outer < len(students) and 0 <= inner < len(students[outer]):
    print(f"students[{outer}][{inner}] =", students[outer][inner])
else:
    print("Index out of range!")

# Loop through all elements
print("\nAll records:")
for roll, name, marks in students:
    print(f"  Roll: {roll}  Name: {name:<6} Marks: {marks}")
