# Q15. Merge dictionaries, adding numeric values for shared keys.

dict1 = {"a": 10, "b": 20, "c": 30}
dict2 = {"b": 5, "c": 7, "d": 12}
merged = dict1.copy()

for key, value in dict2.items():
    if key in merged:
        merged[key] += value
    else:
        merged[key] = value

print("First dictionary:", dict1)
print("Second dictionary:", dict2)
print("Merged dictionary:", merged)
