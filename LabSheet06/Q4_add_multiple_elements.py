# Add multiple elements using update()
items = {1, 2, 3}
values = input("Enter multiple elements separated by spaces: ").split()
items.update(values)
print("Updated set:", items)
