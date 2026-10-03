# Q14: Multiplication table of a given number
number = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{number} x {i:2} = {number * i}")
