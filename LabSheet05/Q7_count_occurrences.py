# Q7: Count the occurrences of an element in a tuple

my_tuple = tuple(input("Enter tuple elements separated by spaces: ").split())
target = input("Enter the element to count: ")

# tuple.count() returns how many times the value appears
occurrences = my_tuple.count(target)

print("Tuple:", my_tuple)
print(f"'{target}' appears {occurrences} time(s)")
