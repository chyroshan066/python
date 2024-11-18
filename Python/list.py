names = ["Roshan", "Prachit", "Sandip", "Prayush", "Sandesh"]

# ACCESSING ELEMENTS OR RANGE OF ELEMENTS IN LIST
# names[0] = "Ram"
# print(names[0:3])
# print(names[0])
# print(names[-1])

# LIST CONSTRUCTOR
# names = list()
# names = list(("Roshan", "Prachit", "Sandip", "Prayush", "Sandesh"))
# names = list("Roshan")
# names = list({1, 2, 4, 3})  # Order is not guaranteed
# names = list({1: "Roshan", 2: "Sandesh"})

# CHANGING RANGE OF VALUES IN LIST
# names[1:3] = ["Mahesh", "Ganesh"]
# names[1:3] = ["Mahesh", "Ganesh", "Prabesh"]  # Inserting items more than specified
names[1:3] = ["Mahesh"]  # Inserting items less than specified

print(names)