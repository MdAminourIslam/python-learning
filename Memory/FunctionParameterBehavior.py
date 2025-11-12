print("\n==== Function Parameter Behavior ====")
def modify_list(g):
    g[0] = 100

def modify_number(x):
    x = 200

lst = [1, 2, 3]
num = 10

modify_list(lst)
modify_number(num)
print("lst after modify_list =", lst)  # [100, 2, 3]
print("num after modify_number =", num)  # 10