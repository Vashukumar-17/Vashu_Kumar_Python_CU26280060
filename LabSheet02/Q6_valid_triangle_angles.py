# Q6: Check whether a triangle is valid given its angles
a = float(input("Enter first angle: "))
b = float(input("Enter second angle: "))
c = float(input("Enter third angle: "))
# Valid if all angles are positive and they sum to 180 degrees
if a > 0 and b > 0 and c > 0 and a + b + c == 180:
    print("The triangle is VALID.")
else:
    print("The triangle is NOT valid.")
