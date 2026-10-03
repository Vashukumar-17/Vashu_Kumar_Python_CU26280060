# Q29: Check if a number is in a given range
low = float(input("Enter lower limit: "))
high = float(input("Enter upper limit: "))
number = float(input("Enter the number to check: "))
if low > high:
    low, high = high, low  # fix reversed limits
if low <= number <= high:
    print(f"{number} lies within the range [{low}, {high}].")
else:
    print(f"{number} lies outside the range [{low}, {high}].")
