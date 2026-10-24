# Q28: Find repeated items in a tuple

my_tuple = tuple(input("Enter tuple elements separated by spaces: ").split())

repeated = ()
for element in my_tuple:
    # An item is repeated if it appears more than once; list each only once
    if my_tuple.count(element) > 1 and element not in repeated:
        repeated += (element,)

print("Tuple          :", my_tuple)
if repeated:
    print("Repeated items :", repeated)
    for item in repeated:
        print(f"  '{item}' appears {my_tuple.count(item)} times")
else:
    print("No repeated items found.")
