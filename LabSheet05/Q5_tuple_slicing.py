# Q5: Access tuple elements using slicing

my_tuple = tuple(input("Enter tuple elements separated by spaces: ").split())
print("Tuple:", my_tuple)

start = int(input("Enter start index: "))
stop = int(input("Enter stop index (exclusive): "))
step = int(input("Enter step (non-zero): "))

if step == 0:
    print("Step cannot be zero!")
else:
    # Syntax: tuple[start:stop:step]
    print(f"my_tuple[{start}:{stop}:{step}] =", my_tuple[start:stop:step])

# A few more slicing examples
print("First three   :", my_tuple[:3])
print("Last three    :", my_tuple[-3:])
print("Every 2nd item:", my_tuple[::2])
print("Reversed      :", my_tuple[::-1])
