# Q18: Check if two tuples are equal

tuple_one = tuple(input("Enter elements of first tuple (space separated): ").split())
tuple_two = tuple(input("Enter elements of second tuple (space separated): ").split())

print("First tuple :", tuple_one)
print("Second tuple:", tuple_two)

# == compares length, order and values of the elements
if tuple_one == tuple_two:
    print("Result: The tuples are EQUAL.")
else:
    print("Result: The tuples are NOT equal.")
    # Same elements in a different order?
    if sorted(tuple_one) == sorted(tuple_two):
        print("Note: They have the same elements but in a different order.")
