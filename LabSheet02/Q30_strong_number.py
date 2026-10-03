# Q30: Check if a number is strong (sum of digit factorials == number)
number = int(input("Enter a positive integer: "))
temp = number
total = 0
while temp > 0:
    digit = temp % 10
    fact = 1
    for i in range(2, digit + 1):  # factorial of the digit
        fact *= i
    total += fact
    temp //= 10
if number > 0 and total == number:
    print(f"{number} is a Strong number.")
else:
    print(f"{number} is NOT a Strong number.")
