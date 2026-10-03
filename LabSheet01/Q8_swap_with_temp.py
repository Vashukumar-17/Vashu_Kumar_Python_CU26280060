# Q8: Swap two variables using a temporary variable
a = input("Enter value of a: ")
b = input("Enter value of b: ")
print(f"Before swap: a = {a}, b = {b}")
temp = a   # store a in temporary variable
a = b
b = temp
print(f"After swap:  a = {a}, b = {b}")
