# Q30: Find the element-wise sum of two tuples

tuple_one = tuple(float(x) for x in input("Enter numbers of first tuple (space separated): ").split())
tuple_two = tuple(float(x) for x in input("Enter numbers of second tuple (space separated): ").split())

if len(tuple_one) != len(tuple_two):
    print("Note: tuples have different lengths; extra elements are ignored.")

# zip() pairs up elements at the same position
result = tuple(a + b for a, b in zip(tuple_one, tuple_two))

print("First tuple     :", tuple_one)
print("Second tuple    :", tuple_two)
print("Element-wise sum:", result)
