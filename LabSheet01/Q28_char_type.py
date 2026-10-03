# Q28: Check if a character is uppercase, lowercase, or a digit
ch = input("Enter a single character: ")
if len(ch) != 1:
    print("Please enter exactly one character.")
elif 'A' <= ch <= 'Z':
    print(f"'{ch}' is an Uppercase letter.")
elif 'a' <= ch <= 'z':
    print(f"'{ch}' is a Lowercase letter.")
elif '0' <= ch <= '9':
    print(f"'{ch}' is a Digit.")
else:
    print(f"'{ch}' is a special character.")
