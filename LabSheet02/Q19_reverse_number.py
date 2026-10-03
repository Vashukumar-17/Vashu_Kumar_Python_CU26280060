# Q19: Reverse a number using a loop
number = int(input("Enter a non-negative integer: "))
temp = number
reversed_number = 0
while temp > 0:
    reversed_number = reversed_number * 10 + temp % 10
    temp //= 10
print(f"Reverse of {number} = {reversed_number}")
