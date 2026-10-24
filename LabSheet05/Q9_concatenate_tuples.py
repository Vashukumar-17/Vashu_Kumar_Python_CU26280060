# Q9: Concatenate two tuples

tuple_one = tuple(input("Enter elements of first tuple (space separated): ").split())
tuple_two = tuple(input("Enter elements of second tuple (space separated): ").split())

# The + operator joins two tuples into a new tuple
combined = tuple_one + tuple_two

print("First tuple  :", tuple_one)
print("Second tuple :", tuple_two)
print("Concatenated :", combined)
