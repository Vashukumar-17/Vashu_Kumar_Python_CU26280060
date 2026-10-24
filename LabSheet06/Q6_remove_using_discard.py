# discard() does not raise an error if the element is absent
items = {1, 2, 3, 4}
try:
    value = int(input("Enter an integer to discard: "))
    items.discard(value)
    print("Updated set:", items)
except ValueError:
    print("Please enter a valid integer.")
