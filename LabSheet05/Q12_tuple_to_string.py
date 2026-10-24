# Q12: Convert a tuple into a string

my_tuple = tuple(input("Enter tuple elements (words or characters) separated by spaces: ").split())

# join() works on tuples of strings
joined_no_space = "".join(my_tuple)
joined_with_space = " ".join(my_tuple)
joined_with_comma = ", ".join(my_tuple)

print("Tuple               :", my_tuple)
print("Joined (no space)   :", joined_no_space)
print("Joined (with space) :", joined_with_space)
print("Joined (with comma) :", joined_with_comma)

# If the tuple holds non-string items, convert each with str() first
number_tuple = (1, 2, 3, 4)
print("Number tuple to str :", "-".join(str(num) for num in number_tuple))
