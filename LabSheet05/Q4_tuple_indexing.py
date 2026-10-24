# Q4: Access tuple elements using indexing

my_tuple = tuple(input("Enter tuple elements separated by spaces: ").split())
size = len(my_tuple)
print("Tuple:", my_tuple)

index = int(input(f"Enter an index (-{size} to {size - 1}): "))

# Valid indexes are from -size to size-1
if -size <= index < size:
    print(f"Element at index {index}: {my_tuple[index]}")
else:
    print("Index out of range!")

# Demonstrate positive and negative indexing
print("First element :", my_tuple[0])
print("Last element  :", my_tuple[-1])
