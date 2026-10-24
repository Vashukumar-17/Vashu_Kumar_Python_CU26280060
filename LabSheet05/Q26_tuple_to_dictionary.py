# Q26: Convert a tuple of tuples into a dictionary

count = int(input("How many (key, value) pairs? "))

pairs = ()
for i in range(count):
    key = input(f"Enter key {i + 1}: ")
    value = input(f"Enter value {i + 1}: ")
    pairs += ((key, value),)  # add a (key, value) tuple

# dict() accepts a sequence of 2-element tuples
result_dict = dict(pairs)

print("\nTuple of tuples :", pairs)
print("Dictionary      :", result_dict)
print("(If a key was repeated, the last value is kept.)")
