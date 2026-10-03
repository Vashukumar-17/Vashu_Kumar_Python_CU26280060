# Q13: Sum of first n natural numbers
n = int(input("Enter n: "))
total = 0
for number in range(1, n + 1):
    total += number
print(f"Sum of first {n} natural numbers = {total}")
