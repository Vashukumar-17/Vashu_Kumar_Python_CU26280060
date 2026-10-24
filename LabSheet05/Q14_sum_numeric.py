# Q14: Calculate the sum of numeric elements in a tuple

raw_items = input("Enter elements (numbers and words allowed) separated by spaces: ").split()


def to_number(text):
    """Return int/float if text is numeric, otherwise return the text unchanged."""
    try:
        return int(text)
    except ValueError:
        try:
            return float(text)
        except ValueError:
            return text


my_tuple = tuple(to_number(item) for item in raw_items)

total = 0
for element in my_tuple:
    # Add only int/float values and skip everything else
    if isinstance(element, (int, float)):
        total += element

print("Tuple               :", my_tuple)
print("Sum of numeric items:", total)
