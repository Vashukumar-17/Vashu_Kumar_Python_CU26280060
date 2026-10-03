# Q24: Check if a given year is a leap year
year = int(input("Enter a year: "))
# Leap if divisible by 400, or divisible by 4 but not by 100
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(f"{year} is a Leap Year.")
else:
    print(f"{year} is NOT a Leap Year.")
