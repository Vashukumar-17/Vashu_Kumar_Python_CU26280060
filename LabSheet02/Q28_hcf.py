# Q28: Find HCF (GCD) of two numbers using a loop
a = int(input("Enter first positive integer: "))
b = int(input("Enter second positive integer: "))
if a <= 0 or b <= 0:
    print("Please enter positive integers.")
else:
    smaller = a if a < b else b
    hcf = 1
    for i in range(1, smaller + 1):
        if a % i == 0 and b % i == 0:  # common divisor
            hcf = i                    # keep the largest
    print(f"HCF of {a} and {b} = {hcf}")
