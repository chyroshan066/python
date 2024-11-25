import re

string = "Hello, my phone$# _number is 9702680657"

# pattern = r"[0-9]"
# pattern = r'\d'  # Returns a match where the string contains the digits

# pattern = r'\D'  # Returns a match where the string doesn't contain the digits

# pattern = r'\w'  # Returns a match where the string contains word characters (numbers + alphabets + underscores)

# pattern = r'\W'  # Returns a match where the string doesn't contain word characters (numbers + alphabets + underscores)

# pattern = r'\s'  # Returns a match where the string contains whitespaces

# pattern = r'\S'  # Returns a match where the string doesn't contain whitespaces

# pattern = r'\bHello,my\b'  # Used for searching the specific words in the text

# pattern = r'\AHello'  # Checks if the specified character is at the beginning of the string or not

# pattern = r'9702680657\Z'  # Checks if the specified character is at the end of the string or not

pattern = r'.'  # Returns all the characters in the string except newline characters

matches = re.finditer(pattern, string)

for match in matches:
    print(match.start(), "-->", match.group(), end="  ")