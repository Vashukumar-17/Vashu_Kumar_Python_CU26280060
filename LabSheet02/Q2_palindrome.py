# Q2: Check if a number is a palindrome
number = int(input("Enter a non-negative integer: "))
temp = number
reversed_number = 0
while temp > 0:
    digit = temp % 10                          # extract last digit
    reversed_number = reversed_number * 10 + digit  # append to reverse
    temp //= 10                                # drop last digit
if reversed_number == number:
    print(f"{number} is a Palindrome.")
else:
    print(f"{number} is NOT a Palindrome.")
