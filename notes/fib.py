def fib(n):
    if n <= 1:
        return n

    return fib(n-1)+fib(n-2)
# 0,1,1,2,3,5,8 ... except for the first 2 which are always 0 and 1


for i in range(30):
    print(f"{i:3} {fib(i)}")

# time complexity o(2^n)
# the higher it goes the slower i gets


# Memoization, top-down dynamic programming
cache = {}


def fib1(n):
    if n <= 1:
        return n

    # test keys, looks for key in cache
    if n not in cache:
        cache[n] = fib1(n-1)+fib1(n-2)
    return cache[n]
# 0,1,1,2,3,5,8 ... except for the first 2 which are always 0 and 1


for i in range(35):
    print(f"{i:3} {fib(i)}")


"""
fib(30)=fib(29)+fib(28)
fib(29)=fib(28)+fib(27)
fib(28)=fib(27)+fib(26)
fib(28)=fib(27)+fib(26)
fib(27)=fib(26)+fib(25)
fib(27)=fib(26)+fib(25)
fib(26)=fib(25)+fib(24)
fib(27)=fib(26)+fib(25)
fib(28)=fib(27)+fib(26)
fib(26)=fib(25)+fib(24)
fib(26)=fib(25)+fib(24)
fib(25)=fib(24)+fib(23)
"""

"""fib1(30)=fib1(29)+fib1(28)
fib1(29)=fib1(28)+fib1(27)
fib1(28)=fib1(27)+fib1(26)
fib1(28)=fib1(27)+fib1(26)
.
.
.
fib1(1)=1 base case"""
