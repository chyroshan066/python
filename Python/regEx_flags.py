import re

text = ("""A tropical.cyclone is a rapidly rotating storm system that forms over warm 123
        Tropical or subtropical waters 456
        Hello mosi mos I am Roshan 789""")
singleLineText = "A tropical.cyclone is a rapidly rotating storm पढाई system that forms over."

'''pattern = r"\btropical\b"
print(re.findall(pattern, text))  # Default is case sensitive matching
# print(re.findall(pattern, text, re.IGNORECASE))  # Does case in-sensitive matching
print(re.findall(pattern, text, re.I))'''

'''pattern = r"\d{3}$"  # Returns the character if it ends with 3 digits
print(re.findall(pattern, text))
print(re.findall(pattern, text, re.MULTILINE))  # Returns the character if it ends with 3 digits. Searches for each line'''

'''pattern = r"."  # Returns the character if it ends with 3 digits
print(re.findall(pattern, text))
print(re.findall(pattern, text, re.S))
print(re.findall(pattern, text, re.DOTALL))  # Returns every characters includes even newline'''

# pattern = r"tropical\.cyclone#mathces data"  # Returns the character if it ends with 3 digits
'''pattern = r"tropical(?#mathces data)\.cyclone"  # Way of adding comments in the middle of pattern. Syntax:  (?#comments)
# print(re.findall(pattern, text))  # Generally doesn't accept comments in pattern
# print(re.findall(pattern, text, re.VERBOSE))  # Accept comments in pattern
print(re.findall(pattern, text, re.X))'''

'''pattern = r'\b\w+\b'
print(re.findall(pattern, singleLineText))
# print(re.findall(pattern, singleLineText, re.ASCII))  # Ignores non-ASCII characters
print(re.findall(pattern, singleLineText, re.A))'''

pattern = re.compile(r'\b\w+\b', re.A)  # When using compile regular expression/function, then flag needs to be passed inside compile function
# print(re.findall(pattern, singleLineText))
print(pattern.findall(singleLineText))