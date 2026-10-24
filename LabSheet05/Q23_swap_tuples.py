# Q23: Swap two tuples

tuple_a = tuple(input("Enter elements of first tuple (space separated): ").split())
tuple_b = tuple(input("Enter elements of second tuple (space separated): ").split())

print("\nBefore swapping:")
print("tuple_a =", tuple_a)
print("tuple_b =", tuple_b)

# Python allows swapping without a temporary variable
tuple_a, tuple_b = tuple_b, tuple_a

print("\nAfter swapping:")
print("tuple_a =", tuple_a)
print("tuple_b =", tuple_b)
