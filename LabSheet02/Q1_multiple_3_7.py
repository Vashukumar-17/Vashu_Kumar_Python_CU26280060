# Q1: Check if a number is a multiple of both 3 and 7
number = int(input("Enter an integer: "))
if number % 3 == 0 and number % 7 == 0:  # both remainders must be zero
    print(f"{number} is a multiple of both 3 and 7.")
else:
    print(f"{number} is NOT a multiple of both 3 and 7.")
