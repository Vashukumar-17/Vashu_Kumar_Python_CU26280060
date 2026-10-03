# Q21: Sum of digits of a number
number = int(input("Enter an integer: "))
if number < 0:
    number = -number
total = 0
while number > 0:
    total += number % 10  # add last digit
    number //= 10
print(f"Sum of digits = {total}")
