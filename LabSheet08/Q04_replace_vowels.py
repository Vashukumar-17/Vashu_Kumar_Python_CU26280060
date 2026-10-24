# Q4. Replace all vowels with * using maketrans() and translate().

text = input("Enter a string: ")
table = str.maketrans("aeiouAEIOU", "**********")
print(text.translate(table))
