# Q22. Read a text file using read(), readline(), and readlines().
# Run Q21 first or ensure student.txt exists in this folder.

filename = "student.txt"

print("--- read() ---")
with open(filename, "r", encoding="utf-8") as file:
    print(file.read(), end="")

print("\n--- readline() ---")
with open(filename, "r", encoding="utf-8") as file:
    while True:
        line = file.readline()
        if not line:
            break
        print(repr(line))

print("\n--- readlines() ---")
with open(filename, "r", encoding="utf-8") as file:
    lines = file.readlines()
    print(lines)
