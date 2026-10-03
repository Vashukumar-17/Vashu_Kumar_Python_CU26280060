# Q17: Factorial of a given number
n = int(input("Enter a non-negative integer: "))
if n < 0:
    print("Factorial is not defined for negative numbers.")
else:
    factorial = 1
    for i in range(2, n + 1):
        factorial *= i
    print(f"{n}! = {factorial}")
