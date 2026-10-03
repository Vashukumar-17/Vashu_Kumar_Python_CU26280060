# Q9: Swap two variables without using a temporary variable
a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))
print(f"Before swap: a = {a}, b = {b}")
a = a + b  # a holds the sum
b = a - b  # b becomes original a
a = a - b  # a becomes original b
print(f"After swap:  a = {a}, b = {b}")
