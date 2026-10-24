# Q6: Check if an element exists in a tuple

my_tuple = tuple(input("Enter tuple elements separated by spaces: ").split())
search_item = input("Enter the element to search for: ")

# The 'in' operator checks membership
if search_item in my_tuple:
    print(f"'{search_item}' EXISTS in the tuple {my_tuple}")
else:
    print(f"'{search_item}' does NOT exist in the tuple {my_tuple}")
