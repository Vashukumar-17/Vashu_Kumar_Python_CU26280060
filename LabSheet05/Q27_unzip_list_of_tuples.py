# Q27: Unzip a list of tuples into individual lists

count = int(input("How many (name, marks) tuples? "))

list_of_tuples = []
for i in range(count):
    name = input(f"Enter name {i + 1}: ")
    marks = int(input(f"Enter marks {i + 1}: "))
    list_of_tuples.append((name, marks))

print("\nList of tuples:", list_of_tuples)

if list_of_tuples:
    # zip(*data) regroups the data column-wise
    names, marks_list = zip(*list_of_tuples)
    names = list(names)
    marks_list = list(marks_list)
    print("Names list    :", names)
    print("Marks list    :", marks_list)
else:
    print("Nothing to unzip.")
