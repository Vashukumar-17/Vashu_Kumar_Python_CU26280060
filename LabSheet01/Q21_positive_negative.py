# Q21: Check if a number is positive or negative
number = float(input("Enter a number: "))
if number > 0:
    print(f"{number} is Positive.")
elif number < 0:
    print(f"{number} is Negative.")
else:
    print("The number is Zero (neither positive nor negative).")
