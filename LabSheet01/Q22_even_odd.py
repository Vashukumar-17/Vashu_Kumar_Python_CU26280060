# Q22: Check if a number is even or odd
number = int(input("Enter an integer: "))
if number % 2 == 0:  # divisible by 2 -> even
    print(f"{number} is Even.")
else:
    print(f"{number} is Odd.")
