# Q1. Check whether a string contains alphabetic characters, alphanumeric characters,
# digits, or whitespace using appropriate string methods.

s = input("Enter a string: ")

print("Only alphabetic characters:", s.isalpha())
print("Only alphanumeric characters:", s.isalnum())
print("Only digits:", s.isdigit())
print("Only whitespace:", s.isspace())
