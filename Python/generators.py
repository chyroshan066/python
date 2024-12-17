# Defining our own iterator using generator function
def topten():
    '''yield 5
    yield 4
    yield 3'''

    n = 1
    while n <= 10:
        yield n**2  # Unlike "return", "yield" doesn't terminate the function
        n += 1

# print(topten())  # Gives the generator object
values = topten()
'''print(next(values))
print(next(values))
print(next(values))'''

my_generator = (num for num in range(10))  # Using generator expression to create generator
print(f"Generated outside loop: {next(my_generator)}")
print(f"Generated outside loop: {next(my_generator)}")

for item in my_generator:  # Generator also works on for loop
    print(item)

print(f"Generator after for loop: {next(my_generator)}")  # Generates error because no value left in the generator