# # This Python file uses the following encoding: utf-8
# import os
# import sys

data = [None, None, None, None, None, None, None, None]


def my_hashing_function(s):
    for c in s:
        print(ord(c))


my_hashing_function('ebii')

print("********====*****")


def my_hashing_function2(s):
    string_bytes = s.encode()
    for b in string_bytes:
        print(b)


my_hashing_function2('@ebii')

print("********====*****")


# 1 funcion turns strng into a number
def my_hash_fun(s):
    string_bytes = s.encode()
    total = 0
    for b in string_bytes:
        total += b
        # total += ord(b)
        # total += int(b)
        # b
    return total


print(my_hash_fun('@ebii'))

# # takes a key and turns it into a

# 2 takes number and makes sure it fits into array
# that number is the index of the array that we're going to store stuff in, or look them up in


def get_slot(s):
    hash_val = my_hash_fun(s)
    return hash_val % len(data)


# print(my_hash_fun('ebii'))
print(get_slot('ebii'))
print(get_slot('foo'))


def get(key):  # order 1 operation o(1)
    slot = get_slot(key)
    return data[slot]


def put(key, value):  # o(1)
    slot = get_slot(key)
    data[slot] = value

# delete option 1


def delete(key):
    slot = get_slot(key)
    data[slot] = None

# delete option2


def delete2(key):
    put(key, None)


put('ebii', 3490)
put('foo', 999)

print(get('ebii'))
print(get('foo'))
print(get('bar'))
print(data)
