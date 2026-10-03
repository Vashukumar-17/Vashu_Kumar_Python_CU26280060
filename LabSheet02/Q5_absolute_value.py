# Q5: Find absolute value of a number (without abs())
number = float(input("Enter a number: "))
if number < 0:
    absolute = -number  # negate negative numbers
else:
    absolute = number
print(f"Absolute value of {number} = {absolute}")
