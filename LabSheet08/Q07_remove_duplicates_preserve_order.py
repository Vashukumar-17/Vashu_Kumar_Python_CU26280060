# Q7. Remove duplicates while preserving original order.

items = input("Enter list elements separated by spaces: ").split()
unique = []

for item in items:
    if item not in unique:
        unique.append(item)

print("List without duplicates:", unique)
