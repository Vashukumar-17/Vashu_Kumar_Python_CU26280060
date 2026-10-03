# Q19: Calculate monthly EMI for a loan
# EMI = P * r * (1+r)^n / ((1+r)^n - 1)
principal = float(input("Enter loan amount: "))
annual_rate = float(input("Enter annual interest rate (%): "))
years = float(input("Enter loan tenure (years): "))
months = int(years * 12)                 # total number of installments
monthly_rate = annual_rate / 12 / 100    # monthly interest rate
if months <= 0:
    print("Error: tenure must be at least one month.")
elif monthly_rate == 0:
    print(f"Monthly EMI = {principal / months:.2f}")  # no interest case
else:
    growth = (1 + monthly_rate) ** months
    emi = principal * monthly_rate * growth / (growth - 1)
    print(f"Monthly EMI   = {emi:.2f}")
    print(f"Total Payment = {emi * months:.2f}")
    print(f"Total Interest= {emi * months - principal:.2f}")
