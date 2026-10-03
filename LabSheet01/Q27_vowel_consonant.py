# Q27: Check if a character is a vowel or consonant
ch = input("Enter a single character: ")
if len(ch) != 1:
    print("Please enter exactly one character.")
elif ('a' <= ch <= 'z') or ('A' <= ch <= 'Z'):
    if ch in "aeiouAEIOU":
        print(f"'{ch}' is a Vowel.")
    else:
        print(f"'{ch}' is a Consonant.")
else:
    print(f"'{ch}' is not an alphabet.")
