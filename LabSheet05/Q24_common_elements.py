# Q24: Find common elements between two tuples

tuple_one = tuple(input("Enter elements of first tuple (space separated): ").split())
tuple_two = tuple(input("Enter elements of second tuple (space separated): ").split())

common = ()
for element in tuple_one:
    # Keep elements present in both tuples (avoid adding the same one twice)
    if element in tuple_two and element not in common:
        common += (element,)

print("First tuple     :", tuple_one)
print("Second tuple    :", tuple_two)
if common:
    print("Common elements :", common)
else:
    print("There are no common elements.")
