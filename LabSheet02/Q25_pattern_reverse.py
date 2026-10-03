# Q25: Print a reverse star pattern
rows = int(input("Enter number of rows: "))
for i in range(rows, 0, -1):
    print("* " * i)  # rows stars first, then fewer
