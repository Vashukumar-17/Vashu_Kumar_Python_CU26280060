# Remove every element of B from A
a = {1, 2, 3, 4, 5}
b = {2, 4}
a.difference_update(b)
print("A after removing elements of B:", a)
