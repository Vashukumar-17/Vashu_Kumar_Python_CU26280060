# Q2: Create a tuple with different data types

# Take different types of input from the user
name = input("Enter your name (str): ")
age = int(input("Enter your age (int): "))
height = float(input("Enter your height in metres (float): "))
is_student = input("Are you a student? (yes/no): ").strip().lower() == "yes"

# Combine all values into one tuple
mixed_tuple = (name, age, height, is_student, None, 3 + 4j)

print("\nTuple:", mixed_tuple)
print("\nElement and its data type:")
for element in mixed_tuple:
    print(f"  {str(element):<10} -> {type(element).__name__}")
