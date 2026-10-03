# Q16: Find the remainder when a number is divided by another
number = int(input("Enter the number: "))
divisor = int(input("Enter the divisor: "))
if divisor == 0:
    print("Error: divisor cannot be zero.")
else:
    remainder = number % divisor  # modulus operator
    print(f"Remainder of {number} / {divisor} = {remainder}")
