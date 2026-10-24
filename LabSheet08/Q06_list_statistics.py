# Q6. Largest, smallest, sum, and average without max() or min().

n = int(input("How many numbers? "))
if n <= 0:
    print("Please enter a positive count.")
else:
    numbers = []
    for i in range(n):
        numbers.append(float(input(f"Enter number {i + 1}: ")))

    largest = smallest = numbers[0]
    total = 0
    for number in numbers:
        if number > largest:
            largest = number
        if number < smallest:
            smallest = number
        total += number

    print("Largest:", largest)
    print("Smallest:", smallest)
    print("Sum:", total)
    print("Average:", total / n)
