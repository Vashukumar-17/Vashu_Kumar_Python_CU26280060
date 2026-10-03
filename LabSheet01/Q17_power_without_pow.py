# Q17: Calculate power of a number without using pow()
base = float(input("Enter base: "))
exponent = int(input("Enter exponent (integer): "))
count = exponent if exponent >= 0 else -exponent  # work with |exponent|
result = 1
for _ in range(count):
    result = result * base  # repeated multiplication
if exponent < 0:
    if base == 0:
        print("Error: 0 cannot be raised to a negative power.")
        raise SystemExit
    result = 1 / result  # negative exponent -> reciprocal
print(f"{base} ^ {exponent} = {result}")
