# Q2. Find first and last occurrence using find(), rfind(), index(), and rindex().

text = input("Enter the main string: ")
sub = input("Enter the substring to search: ")

first = text.find(sub)
last = text.rfind(sub)
print("find() first occurrence:", first)
print("rfind() last occurrence:", last)

if first == -1:
    print("Substring not found; index() and rindex() would raise ValueError.")
else:
    print("index() first occurrence:", text.index(sub))
    print("rindex() last occurrence:", text.rindex(sub))
