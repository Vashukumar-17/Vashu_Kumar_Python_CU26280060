# Q4: Divide two integers and display quotient and remainder
dividend = int(input("Enter dividend: "))
divisor = int(input("Enter divisor: "))
if divisor == 0:
    # division by zero is undefined
    print("Error: divisor cannot be zero.")
else:
    quotient = dividend // divisor   # floor division gives quotient
    remainder = dividend % divisor   # modulus gives remainder
    print(f"Quotient  = {quotient}")
    print(f"Remainder = {remainder}")
