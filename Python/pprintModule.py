import pprint

data = {
    "name": "Roshan Chaudhary",
    "age": 21,
    "cities": ["Birtamode", "Biratnagar", "Dharan"],
    "skills": {"python": "Intermediate",
               "javascript": "Advanced",
               "C++": "Intermediate",
               }
}

# pprint.pprint(data)  # Makes output prettier and readable
pprint.pprint(data, indent=2, depth=2)
# print(data)