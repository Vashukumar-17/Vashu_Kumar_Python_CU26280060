# Q9: Check eligibility for voting
age = int(input("Enter your age: "))
if age < 0:
    print("Invalid age.")
elif age >= 18:
    print("You are eligible to vote.")
else:
    print(f"You are NOT eligible to vote. Wait {18 - age} more year(s).")
