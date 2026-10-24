# remove() raises KeyError if the element is absent
items = {1, 2, 3, 4}
try:
    value = int(input("Enter an integer to remove: "))
    items.remove(value)
    print("Updated set:", items)
except KeyError:
    print("That element is not in the set.")
except ValueError:
    print("Please enter a valid integer.")
