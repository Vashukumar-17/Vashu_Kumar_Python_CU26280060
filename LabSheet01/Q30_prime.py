# Q30: Check if a number is prime
number = int(input("Enter an integer: "))
if number < 2:
    print(f"{number} is NOT a prime number.")
else:
    is_prime = True
    divisor = 2
    while divisor * divisor <= number:  # only check up to sqrt(number)
        if number % divisor == 0:
            is_prime = False
            break
        divisor += 1
    if is_prime:
        print(f"{number} is a Prime number.")
    else:
        print(f"{number} is NOT a prime number.")
