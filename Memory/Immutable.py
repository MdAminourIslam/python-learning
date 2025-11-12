print("==== Immutable Example (int, str, tuple) ====")
a = 10
b = a
b = 20
print("a =", a)   # 10 (unchanged, because int is immutable)
print("b =", b)   # 20

s1 = "hello"
s2 = s1
s2 = s2.upper()
print("s1 =", s1)  # "hello"
print("s2 =", s2)  # "HELLO"

t1 = (1, 2, 3)
t2 = t1
# t2[0] = 99   # ❌ ERROR: tuple is immutable
print("t1 =", t1)
print("t2 =", t2)