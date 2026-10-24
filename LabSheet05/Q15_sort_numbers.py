# Q15: Sort a tuple of numbers in ascending order

numbers = tuple(float(x) for x in input("Enter numbers separated by spaces: ").split())

# Tuples are immutable, so sorted() builds a new sorted sequence
# which we convert back into a tuple
sorted_numbers = tuple(sorted(numbers))

print("Original tuple :", numbers)
print("Sorted (asc)   :", sorted_numbers)
