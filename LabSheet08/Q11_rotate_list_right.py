# Q11. Rotate a list right by K positions using slicing.

items = input("Enter list elements separated by spaces: ").split()
k = int(input("Enter K: "))

if items:
    k %= len(items)
    rotated = items[-k:] + items[:-k] if k else items[:]
else:
    rotated = []

print("Rotated list:", rotated)
