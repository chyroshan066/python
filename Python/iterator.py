lists = [1, 2, 3, 4]

it  = iter(lists)  # "iter()" function converts the given collection to iterator and iterator gives only one value at a time

print(it.__next__())  # "__init__()" function preserves the old value and gives you the next value
print(it.__next__())

print(next(it))  # "__init__()" function and "next()" function does the same task