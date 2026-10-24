# Q12. Find second-largest distinct value without sort() or sorted().

numbers = list(map(int, input("Enter integers separated by spaces: ").split()))
largest = None
second_largest = None

for number in numbers:
    if largest is None or number > largest:
        if number != largest:
            second_largest = largest
        largest = number
    elif number != largest and (second_largest is None or number > second_largest):
        second_largest = number

if second_largest is None:
    print("No second-largest distinct element exists.")
else:
    print("Second-largest distinct element:", second_largest)
