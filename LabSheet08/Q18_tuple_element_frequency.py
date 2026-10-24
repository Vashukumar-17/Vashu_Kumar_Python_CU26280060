# Q18. Count tuple element frequencies in a dictionary.

items = tuple(input("Enter elements separated by spaces: ").split())
frequency = {}

for item in items:
    frequency[item] = frequency.get(item, 0) + 1

print("Tuple:", items)
print("Frequencies:", frequency)
