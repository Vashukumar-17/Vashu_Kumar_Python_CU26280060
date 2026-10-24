# Q13. Add, update, retrieve, and delete student records.

students = {"Amit": 78, "Priya": 91, "Ravi": 84}

while True:
    print("\n1. Add student  2. Update marks  3. Retrieve marks  4. Delete student  5. Display all  0. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        name = input("Student name: ")
        marks = float(input("Marks: "))
        students[name] = marks
        print("Student added.")
    elif choice == "2":
        name = input("Student name to update: ")
        if name in students:
            students[name] = float(input("New marks: "))
            print("Marks updated.")
        else:
            print("Student not found.")
    elif choice == "3":
        name = input("Student name: ")
        if name in students:
            print("Marks:", students[name])
        else:
            print("Student not found.")
    elif choice == "4":
        name = input("Student name to delete: ")
        if name in students:
            del students[name]
            print("Student deleted.")
        else:
            print("Student not found.")
    elif choice == "5":
        print(students)
    elif choice == "0":
        break
    else:
        print("Invalid choice.")
