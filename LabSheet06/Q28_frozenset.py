# frozenset is immutable: elements cannot be added or removed
items = frozenset({1, 2, 3, 2})
print("Frozen set:", items)
print("Contains 2:", 2 in items)
print("Union with {3, 4}:", items | {3, 4})
try:
    items.add(5)
except AttributeError:
    print("Cannot add elements: frozenset is immutable.")
