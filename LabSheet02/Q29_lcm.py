# Q29: Find LCM of two numbers using a loop
a = int(input("Enter first positive integer: "))
b = int(input("Enter second positive integer: "))
if a <= 0 or b <= 0:
    print("Please enter positive integers.")
else:
    lcm = a if a > b else b
    while lcm % a != 0 or lcm % b != 0:  # search upward for common multiple
        lcm += 1
    print(f"LCM of {a} and {b} = {lcm}")
