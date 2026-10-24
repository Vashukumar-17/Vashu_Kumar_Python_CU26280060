# Set-based check: compares distinct characters, not character counts.
# For a full anagram check, use sorted strings so repeated letters matter.
first = input("Enter first string: ").replace(" ", "").casefold()
second = input("Enter second string: ").replace(" ", "").casefold()
if sorted(first) == sorted(second):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")
