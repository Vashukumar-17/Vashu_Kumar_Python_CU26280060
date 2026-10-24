# Q22: Flatten a nested tuple

import ast  # standard library, used to safely read a tuple typed by the user


def flatten(nested):
    """Recursively flatten a nested tuple into a single tuple."""
    flat = ()
    for item in nested:
        if isinstance(item, tuple):
            flat += flatten(item)  # go deeper for inner tuples
        else:
            flat += (item,)
    return flat


text = input("Enter a nested tuple, e.g. (1, (2, 3), (4, (5, 6))) [press Enter for sample]: ").strip()
if text == "":
    text = "(1, (2, 3), (4, (5, 6)), 7)"

try:
    nested_tuple = ast.literal_eval(text)
    if not isinstance(nested_tuple, tuple):
        print("Please enter a valid tuple!")
    else:
        print("Nested tuple    :", nested_tuple)
        print("Flattened tuple :", flatten(nested_tuple))
except (ValueError, SyntaxError):
    print("Invalid input! Enter a proper tuple like (1, (2, 3)).")
