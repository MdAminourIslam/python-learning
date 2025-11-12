print("\n==== Mutable Example (list, dict, set) ====")
lst1 = [1, 2, 3]
lst2 = lst1
lst2[0] = 99
print("lst1 =", lst1)  # [99, 2, 3] (changed)
print("lst2 =", lst2)  # [99, 2, 3]

d1 = {"x": 1}
d2 = d1
d2["y"] = 2
print("d1 =", d1)  # {"x":1, "y":2}
print("d2 =", d2)


s1 = set()
s1.add(1)
s1.add(2)
s2 = s1
s2.add(5)
print(f"s1 = {s1}")
print(f"s2 = {s2}")


