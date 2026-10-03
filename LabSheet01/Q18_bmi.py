# Q18: Calculate Body Mass Index (BMI)
weight = float(input("Enter weight in kg: "))
height = float(input("Enter height in meters: "))
if height <= 0:
    print("Error: height must be greater than zero.")
else:
    bmi = weight / (height ** 2)  # BMI = kg / m^2
    print(f"BMI = {bmi:.2f}")
    if bmi < 18.5:
        print("Category: Underweight")
    elif bmi < 25:
        print("Category: Normal weight")
    elif bmi < 30:
        print("Category: Overweight")
    else:
        print("Category: Obese")
