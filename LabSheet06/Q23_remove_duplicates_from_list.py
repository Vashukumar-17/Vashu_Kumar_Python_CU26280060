# Remove duplicates; this preserves the first-occurrence order
values = input("Enter list elements separated by spaces: ").split()
unique_values = list(dict.fromkeys(values))
print("List without duplicates:", unique_values)
# Set-only alternative (order is not guaranteed): print(set(values))
