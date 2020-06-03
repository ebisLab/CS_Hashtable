import math
# Inverse square root

# square root is an expensive computation

# inv_sqrt(x)=1/sqrt(x)

inv_sqrt = {}


def build_lookup_table():
    for i in range(1, 1000):
        inv_sqrt[i] = 1 / math.sqrt(i)


build_lookup_table()

print(inv_sqrt[3])
print(inv_sqrt[12])

# google fast inverse
