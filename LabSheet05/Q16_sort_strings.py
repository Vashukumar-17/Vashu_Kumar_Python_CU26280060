# Q16: Sort a tuple of strings alphabetically

words = tuple(input("Enter words separated by spaces: ").split())

# key=str.lower makes the sort case-insensitive
sorted_words = tuple(sorted(words, key=str.lower))

print("Original tuple :", words)
print("Sorted (A-Z)   :", sorted_words)
print("Sorted (Z-A)   :", tuple(sorted(words, key=str.lower, reverse=True)))
