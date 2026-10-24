# Q13: Find the maximum and minimum values in a tuple

numbers = tuple(float(x) for x in input("Enter numbers separated by spaces: ").split())

if len(numbers) == 0:
    print("The tuple is empty!")
else:
    print("Tuple   :", numbers)
    print("Maximum :", max(numbers))
    print("Minimum :", min(numbers))
