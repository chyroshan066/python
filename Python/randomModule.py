import random

for i in range(3):
    # print(random.random())  # Generates random floating point number between 0 and 1
    
    # print(random.randint(10, 20))  # Generates random number between given range

    # print(random.randrange(10, 20, 2))  # Generates random number between given range

    x = random.uniform(10, 20)  # Generates random floating point number between given range

    # print(round(x))  # Rounds the number
    print(round(x, 5))  # Rounds the number until last five digits

myList = ["Roshna", "Roshan", "Roshnee", "Rahul"]
# print(random.choice(myList))  # Selects random element from the given sequence

# print(random.sample(myList, 3))  # Returns a sample from the sequence