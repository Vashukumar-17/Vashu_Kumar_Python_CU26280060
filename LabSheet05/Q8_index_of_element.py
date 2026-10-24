# Q8: Find the index of an element in a tuple

my_tuple = tuple(input("Enter tuple elements separated by spaces: ").split())
target = input("Enter the element to find: ")

print("Tuple:", my_tuple)

# index() raises ValueError if missing, so check first
if target in my_tuple:
    first_index = my_tuple.index(target)
    print(f"First index of '{target}': {first_index}")

    # Show every position where the element occurs
    all_positions = tuple(i for i in range(len(my_tuple)) if my_tuple[i] == target)
    print(f"All positions of '{target}': {all_positions}")
else:
    print(f"'{target}' is not present in the tuple.")
