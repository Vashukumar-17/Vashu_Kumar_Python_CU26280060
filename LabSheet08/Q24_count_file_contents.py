# Q24. Count lines, words, characters, and vowels in a text file.

filename = input("Enter filename (e.g. student.txt): ")

try:
    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()

    lines = len(content.splitlines())
    words = len(content.split())
    characters = len(content)
    vowels = sum(1 for char in content if char.lower() in "aeiou")

    print("Lines:", lines)
    print("Words:", words)
    print("Characters (including spaces and newline characters):", characters)
    print("Vowels:", vowels)
except FileNotFoundError:
    print("File not found. Check the filename and location.")
