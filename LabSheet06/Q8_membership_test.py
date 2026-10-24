# Check whether an element exists in a set
items = {10, 20, 30, 40}
try:
    value = int(input("Enter an integer to search for: "))
    print(value, "exists in set:", value in items)
except ValueError:
    print("Please enter a valid integer.")
