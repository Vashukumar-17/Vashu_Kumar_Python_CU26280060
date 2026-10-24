# Q25: Find the difference between two tuples

tuple_one = tuple(input("Enter elements of first tuple (space separated): ").split())
tuple_two = tuple(input("Enter elements of second tuple (space separated): ").split())


def difference(first, second):
    """Return elements that are in 'first' but not in 'second'."""
    result = ()
    for element in first:
        if element not in second and element not in result:
            result += (element,)
    return result


print("First tuple          :", tuple_one)
print("Second tuple         :", tuple_two)
print("In first, not second :", difference(tuple_one, tuple_two))
print("In second, not first :", difference(tuple_two, tuple_one))
print("Symmetric difference :", difference(tuple_one, tuple_two) + difference(tuple_two, tuple_one))
