s = {"Roshan", 1, True, 3}

# CREATING AN EMPTY SET
# empty_set = {}  # This will not be an empty set but instead be an empty dictionary
empty_set = set()  # This is the correct way of creating set using set() constructor
# print(type(empty_set))

set_comprehension = {element**2 for element in range(10)}
print(set_comprehension)

# print(s)