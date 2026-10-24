# Q20. Check subset, superset, and disjoint relationships.

set_a = set(map(int, input("Enter integers for set A: ").split()))
set_b = set(map(int, input("Enter integers for set B: ").split()))

print("A is subset of B:", set_a.issubset(set_b))
print("A is superset of B:", set_a.issuperset(set_b))
print("B is subset of A:", set_b.issubset(set_a))
print("B is superset of A:", set_b.issuperset(set_a))
print("Sets are disjoint:", set_a.isdisjoint(set_b))
