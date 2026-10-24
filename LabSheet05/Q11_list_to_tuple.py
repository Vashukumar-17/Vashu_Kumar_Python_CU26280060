# Q11: Convert a list into a tuple

# Build a list from user input
my_list = input("Enter list elements separated by spaces: ").split()

# tuple() converts any iterable (here a list) into a tuple
my_tuple = tuple(my_list)

print("List  :", my_list, "->", type(my_list).__name__)
print("Tuple :", my_tuple, "->", type(my_tuple).__name__)
