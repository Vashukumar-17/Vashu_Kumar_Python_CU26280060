# Q1: Create and display a tuple

# Take space-separated values from the user
values = input("Enter elements separated by spaces: ").split()

# Convert the collected values into a tuple
my_tuple = tuple(values)

print("Tuple created :", my_tuple)
print("Type          :", type(my_tuple))

# Other ways to create tuples
empty_tuple = ()
single_element_tuple = (5,)  # the trailing comma is required
print("Empty tuple   :", empty_tuple)
print("Single element:", single_element_tuple)
