# Q26: Print a pyramid pattern of numbers
rows = int(input("Enter number of rows: "))
for i in range(1, rows + 1):
    print(" " * (rows - i), end="")        # leading spaces
    for j in range(1, i + 1):              # ascending numbers
        print(j, end="")
    for j in range(i - 1, 0, -1):          # descending numbers
        print(j, end="")
    print()
