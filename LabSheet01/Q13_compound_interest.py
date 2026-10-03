# Q13: Calculate compound interest (compounded annually)
principal = float(input("Enter principal amount: "))
rate = float(input("Enter annual rate of interest (%): "))
time = float(input("Enter time (years): "))
amount = principal * (1 + rate / 100) ** time  # A = P(1 + r/100)^t
compound_interest = amount - principal         # CI = A - P
print(f"Compound Interest = {compound_interest:.2f}")
print(f"Total Amount      = {amount:.2f}")
