# Q3: Check if a number is an Armstrong number
number = int(input("Enter a non-negative integer: "))
# Step 1: count digits
digit_count = 0
temp = number
while temp > 0:
    digit_count += 1
    temp //= 10
if number == 0:
    digit_count = 1
# Step 2: sum of each digit raised to number of digits
total = 0
temp = number
while temp > 0:
    digit = temp % 10
    total += digit ** digit_count
    temp //= 10
if total == number:
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is NOT an Armstrong number.")
