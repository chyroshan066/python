def invoice(username, amount, due_date):
    print(f"Hello {username}")
    print(f"Your amount to be paid is Rs.{amount:.2f} with a due date of: {due_date}")

# invoice("Prateek", 1500, "Mangshir 04")

# RETURNING A FUNCTION
def create_name(fname, lname):
    fname = fname.capitalize()
    lname = lname.capitalize()
    return fname + " " + lname

fullname= create_name("Roshan", "chaudhary")
# print(fullname)

array = [1, 2, 4, 6]
# print(*array)  # Unpacking of array

# ARBITRARY ARGUMENTS (*args)
def order_coffee(type, *flavor):
    print(f"Bring {type} tea and also show me the various flavors like:")
    for x in flavor:
        print(f"- {x}")

# order_chai("masala", "wine", "whiskey", "cigarette")

# ARBITRARY KEYWORD ARGUMENTS (*kwargs)
def order_chai(type, **details):
    print(f"Bring {type} tea in the following details:")
    for key,value in details.items():
        print(f"- {key}: {value}")

# order_chai("milk", location="Birtamode", time="evening")

# DEFAULT PARAMETER VALUE
def intro(location = "Nepal"):
    print(f"I am from {location}")

# intro("Sweden")
intro()