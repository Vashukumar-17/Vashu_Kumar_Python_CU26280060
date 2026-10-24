# Q29: Check if all elements in a tuple are the same

my_tuple = tuple(input("Enter tuple elements separated by spaces: ").split())

if len(my_tuple) == 0:
    print("The tuple is empty!")
else:
    # Compare every element with the first one
    all_same = True
    for element in my_tuple:
        if element != my_tuple[0]:
            all_same = False
            break

    print("Tuple:", my_tuple)
    if all_same:
        print("Result: All elements are the SAME.")
    else:
        print("Result: All elements are NOT the same.")
