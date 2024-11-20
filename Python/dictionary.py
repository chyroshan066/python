'''dictionary = {
    "name": "Roshan Chaudhary",
    "email": "chyroshan066@gmail.com",
    "Phone": 9702680657,
    # "Phone": 9807950330  # doesn't allows duplication of keys
}'''

# CREATING DICTIONARY USING dict() CONSTRUCTOR
dictionary = dict({
    "name": "Roshan Chaudhary",
    "email": "chyroshan066@gmail.com",
    "Phone": 9702680657,
})

# ACCESSING ELEMENTS
# print(dictionary["name"])
# print(dictionary["password"])  # Generates error because the key doesn't exist

# print(dictionary.get("name"))
# print(dictionary.get("password"))  # Instead of generating error, gives "None" output
# print(dictionary.get("password", "roshanCHY#123"))  # Now, in this case, instead of getting "None", you will get the value "roshanCHY#123"

veiw_all_keys = dictionary.keys()  # Return a list of all the keys

# ADDING ELEMENTS IN DICTIONARY
dictionary["password"] = "roshanCHY#123"

# CHANGING ITEMS
# dictionary.update({"name": "Rakesh Thapa"})  # Updates the dictionary with the items from the given argument
'''dictionary2 = {
    "name": "Mohit Chauhan",
    "Address": "Mumbai",
}'''
# We can also pass a list of key:value pairs to update its value
dictionary2 = [
    ("name", "Mohit Chauhan"),
    ("Address", "Kolkata")
]
dictionary.update(dictionary2)  # Update method just updates the calling object. It doesn't return any value

# REMOVING ITEMS
'''print(dictionary)
print(dictionary.popitem())  # Removes and return the last item from the dictionary'''

# NESTED DICTIONARIES
'''products = {
    "myStock1": {
        "Product": "SSD",
        "Price": 3000,
        "Quantity": 100,
        "InStock": "YES"
    },
    "myStock2": {
        "Product": "HDD",
        "Price": 2500,
        "Quantity": 50,
        "InStock": "YES"
    },
    "myStock3": {
        "Product": "Headphone",
        "Price": 2800,
        "Quantity": 40,
        "InStock": "YES"
    },
    "myStock4": {
        "Product": "Earphone",
        "Price": 1500,
        "Quantity": 10,
        "InStock": "NO"
    },
}
print(products["myStock3"]["Product"])'''

# DICTIONARY METHODS
'''keys = ['key1', 'key2', 'key3', 'key2']
# values = 0
value2 = ['apple', 'mango', 'orange']
# new_dict = dict.fromkeys(keys, values)  # Returns a new dictionary with the specified keys:value pair
# new_dict = dict.fromkeys(keys)  # When you don't pass any value, then it will assign "None" values to every key
# new_dict = dict.fromkeys([])  # With no keys passed, it forms empty dictionary
# new_dict = dict.fromkeys(keys, value2)  # In this case, it will assign keys:value pair in specific order
new_dict = dict.fromkeys(set(keys), 0)
print(new_dict)'''

# print(dictionary.setdefault('name'))  # Returns the value of the key if it is present
# print(dictionary.setdefault('school'))  # If the key is not present then it will not return any value but add that key to the dictionary. If value is not mentioned then it will assign "None" to that key
# print(dictionary.setdefault('school', 'Abacus'))  # When value is specified then it will assign that value to that key in case the key is not present
print(dictionary.setdefault('name', 'Abacus'))

print(dictionary)