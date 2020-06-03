# lets sort a dictionary/hash table

# sort output based on keys or values

a = {"a": 2, "b": 3}

# need to convert thisi nto a list

a.items()
# dict_items([('a', 2), ('b', 3)])
list(a.items())
[('a', 2), ('b', 3)]
sorted(list(a.items()))

# i can sort it --- by default it sorts by key
# .sorted = returns a new list
# .sort = sorts it in place


d = {
    "foo": 12,
    "bar": 17,
    "qux": 2
}

print('d.values --->', d.values())
items = list(d.items())

# sort ascending by key
items.sort()
print('items1-->', items)

# sort descending by key
items.sort(reverse=True)
print('items2-->', items)
print('dictionary items**', dict(items))

# sort ascending by value


"""def get_key(e):  # e is touple
    # return the thing that we want to sort by
    return e[1]  # sort by that element number 1


items.sort(key=get_key)

print('items--->', items)

items.sort(key=get_key, reverse=True)"""

# lambda functions
items.sort(key=lambda e: e[1])

print(items)
