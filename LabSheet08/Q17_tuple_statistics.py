# Q17. Display maximum, minimum, sum, length, and count of a specified element.

numbers = tuple(map(int, input("Enter integers separated by spaces: ").split()))
if not numbers:
    print("The tuple is empty.")
else:
    target = int(input("Enter element to count: "))
    print("Tuple:", numbers)
    print("Maximum:", max(numbers))
    print("Minimum:", min(numbers))
    print("Sum:", sum(numbers))
    print("Length:", len(numbers))
    print("Occurrences of", target, ":", numbers.count(target))
