# Q10. Separate even and odd numbers.

numbers = list(map(int, input("Enter integers separated by spaces: ").split()))
even = []
odd = []

for number in numbers:
    if number % 2 == 0:
        even.append(number)
    else:
        odd.append(number)

print("Even numbers:", even)
print("Odd numbers:", odd)
