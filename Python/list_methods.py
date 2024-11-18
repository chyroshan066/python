name = ["Ram", "Shyam", "Hari"]

# name.append("Gopal")  # Adds an element at the end of the list
# name.append(["Ayush", "Piyush"])

# name.extend(["Ayush", "Piyush"])  # Adds the element of the list to the end of the current list

# name.insert(0, "Piyush")  # Insert the elements at the given index

# del name[2]  # deletes an element from the list

# print(name.pop(2))  # Removes as well as returns the element from the list

# name.remove("Shyam")  # Removes the item with the specified value

# name.clear()  # Removes all the elements from the list

'''name2 = name.copy()  # Returns the copy of the list
print(name2)'''

# name.reverse()  # Reverses the order of the list

# name.sort()  # Sort the list in ascending order. Doesn't return the new list
# name.sort(reverse = True)  # Sort the list in descending order.
items = [
    ("Product1", 10),
    ("Product2", 8),
    ("Product3", 13),
]
'''def myFunc(item):
    return item[1]'''
items.sort(key = lambda item: item[1])
print(items)

# print(sorted(name))  # Returns the sorted list
# print(sorted(name, reverse=True))
# print(name)