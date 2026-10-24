# Q17: Reverse a tuple

my_tuple = tuple(input("Enter tuple elements separated by spaces: ").split())

# Slicing with step -1 reverses the tuple
reversed_tuple = my_tuple[::-1]

print("Original tuple :", my_tuple)
print("Reversed tuple :", reversed_tuple)
