# Q20: Count the number of digits in a number
number = int(input("Enter an integer: "))
if number < 0:
    number = -number  # ignore the sign
count = 0
if number == 0:
    count = 1
while number > 0:
    count += 1
    number //= 10
print(f"Number of digits = {count}")
