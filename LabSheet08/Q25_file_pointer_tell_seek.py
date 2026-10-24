# Q25. Demonstrate tell() and seek().

filename = input("Enter filename (e.g. student.txt): ")

try:
    with open(filename, "r", encoding="utf-8") as file:
        print("Initial pointer position:", file.tell())
        print("First 10 characters:", repr(file.read(10)))
        print("Position after reading:", file.tell())

        position = int(input("Enter a position to seek to: "))
        file.seek(position)
        print("Position after seek():", file.tell())
        print("Remaining contents:")
        print(file.read())
except FileNotFoundError:
    print("File not found. Check the filename and location.")
except (ValueError, OSError) as error:
    print("Could not seek to that position:", error)
