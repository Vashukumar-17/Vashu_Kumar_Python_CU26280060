# Find common characters, ignoring letter case
first = input("Enter first string: ").casefold()
second = input("Enter second string: ").casefold()
common = set(first) & set(second)
common.discard(" ")
print("Common letters:", common)
