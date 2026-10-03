# Q18: Print Fibonacci series up to n terms
n = int(input("Enter number of terms: "))
first, second = 0, 1
print("Fibonacci series:", end=" ")
for _ in range(n):
    print(first, end=" ")
    first, second = second, first + second  # shift the pair forward
print()
