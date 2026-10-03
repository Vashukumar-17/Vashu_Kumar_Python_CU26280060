# Q8: Check if a string contains a particular substring
text = input("Enter the main string: ")
sub = input("Enter the substring to search: ")
found = False
# slide a window of the substring's length over the text
for start in range(len(text) - len(sub) + 1):
    if text[start:start + len(sub)] == sub:
        found = True
        print(f"Substring found at index {start}.")
        break
if not found:
    print("Substring NOT found.")
