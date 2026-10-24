# Generate the power set (all subsets) of a set
from itertools import chain, combinations

def power_set(items):
    values = list(items)
    return [set(combo) for r in range(len(values) + 1)
            for combo in combinations(values, r)]

items = {1, 2, 3}
print("Power set:")
for subset in power_set(items):
    print(subset)
