'''try:
    age = int(input("Age: "))
    if age < 0:
        raise ValueError
    print(age)
except ValueError:
    print("Invalid age")'''

'''try:
    age = int(input("Age: "))
    if age < 0:
        raise ValueError("Invalid age")
    print(age)
except ValueError as var:
    print(var)'''

# CREATING USER DEFINED EXCEPTION
# creating "FiveDivisionError" class which is inherited from "Exception" built in class
class FiveDivisionError(Exception):
    def __init__(self):
        print("Cannot divide by 5")
    # pass

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    if denominator == 5:
        # raise FiveDivisionError("Cannot divide by 5")
        raise FiveDivisionError
    value = numerator / denominator
    print(value)
except (ZeroDivisionError, FiveDivisionError) as var:
    print(var, end="")

print("Rest of code")
