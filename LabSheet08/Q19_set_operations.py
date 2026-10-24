# Q19. Union, intersection, difference, and symmetric difference.

set_a = set(map(int, input("Enter integers for set A: ").split()))
set_b = set(map(int, input("Enter integers for set B: ").split()))

print("Union:", set_a | set_b)
print("Intersection:", set_a & set_b)
print("A - B:", set_a - set_b)
print("B - A:", set_b - set_a)
print("Symmetric difference:", set_a ^ set_b)
