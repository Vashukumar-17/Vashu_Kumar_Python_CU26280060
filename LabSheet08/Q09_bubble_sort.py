# Q9. Bubble sort in ascending order without sort() or sorted().

numbers = list(map(int, input("Enter integers separated by spaces: ").split()))
n = len(numbers)

for i in range(n - 1):
    swapped = False
    for j in range(n - 1 - i):
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
            swapped = True
    if not swapped:
        break

print("Sorted list:", numbers)
