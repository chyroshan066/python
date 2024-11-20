# this_tuple = (1, 2, 3, 4, 3)
# this_tuple[0] = 5  # Not possible in tuple
# print(this_tuple)

# TUPLE METHODS
# print(this_tuple.count(3))  # Returns the occurence of elements
# print(this_tuple.index(4))  # Returns the index of the element

# CREATING TUPLE WITH ONE ELEMENT
# tuples = 1, 2, 3  # We can also create tuple in this way
# tuples = (1)  # This will be an integer
tuples = (1,)
# print(type(tuples))

# TUPLE CONSTRUCTOR
# tuples = tuple([1, 2, 3, 4, 3])
# tuples = tuple("123")
# tuples = tuple({1, 2, 3, 4, 6, 5})  # Order is not maintained
'''tuples = tuple({"a": 1, "b": 2})
print(tuples)
print(type(tuples))'''

# CHANGING TUPLE VALUES
'''this_list = list(this_tuple)
this_list.append("cherry")
this_tuple = tuple(this_list)
print(this_tuple)'''

# UNPACKING A TUPLE USING ASTERISK
# (x, *y, z) = this_tuple
''''(x, y, *z) = this_tuple
# (x, *y, *z) = this_tuple  # Generates runtime error
print(x)
print(y)
print(z)'''

# JOINING TWO OR MORE TUPLES
this_tuple2 = ("Apple", "Banana", "Mango")
'''joined_tuple = this_tuple + this_tuple2
print(joined_tuple)'''

# MULTIPLYING THE CONTENTS OF TUPLE
multiplied_tuple = this_tuple2 * 3
print(multiplied_tuple)