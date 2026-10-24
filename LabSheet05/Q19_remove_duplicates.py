# Q19: Remove duplicate elements from a tuple

my_tuple = tuple(input("Enter tuple elements separated by spaces: ").split())

unique_tuple = ()
for element in my_tuple:
    # Add the element only if we have not seen it before (keeps original order)
    if element not in unique_tuple:
        unique_tuple += (element,)

print("Original tuple :", my_tuple)
print("Without duplicates:", unique_tuple)
