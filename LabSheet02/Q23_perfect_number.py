# Q23: Check if a number is perfect (sum of proper divisors == number)
number = int(input("Enter a positive integer: "))
divisor_sum = 0
for i in range(1, number):
    if number % i == 0:
        divisor_sum += i
if number > 0 and divisor_sum == number:
    print(f"{number} is a Perfect number.")
else:
    print(f"{number} is NOT a Perfect number.")
