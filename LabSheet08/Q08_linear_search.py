# Q8. Linear search and display the position (1-based).

items = input("Enter list elements separated by spaces: ").split()
target = input("Enter element to search: ")

found_index = -1
for i in range(len(items)):
    if items[i] == target:
        found_index = i
        break

if found_index == -1:
    print("Element not found.")
else:
    print("Element found at position:", found_index + 1)
