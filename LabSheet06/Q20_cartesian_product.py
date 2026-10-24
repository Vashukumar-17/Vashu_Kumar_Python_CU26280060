# Cartesian product: all ordered pairs (x, y)
a = {1, 2}
b = {"x", "y"}
product = {(x, y) for x in a for y in b}
print("Cartesian product:", product)
