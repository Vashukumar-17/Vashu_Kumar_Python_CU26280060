# Find maximum and minimum values in a non-empty set
values = set(map(int, input("Enter integers separated by spaces: ").split()))
if values:
    print("Maximum:", max(values))
    print("Minimum:", min(values))
else:
    print("The set is empty; max/min are undefined.")
