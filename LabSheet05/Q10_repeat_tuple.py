# Q10: Repeat a tuple n times

my_tuple = tuple(input("Enter tuple elements separated by spaces: ").split())
n = int(input("Enter the number of repetitions (n): "))

# The * operator repeats the tuple
if n < 0:
    print("n must be 0 or greater!")
else:
    repeated = my_tuple * n
    print("Original tuple:", my_tuple)
    print(f"Repeated {n} times:", repeated)
