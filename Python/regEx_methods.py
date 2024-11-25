import re

# pattern = "waters"
pattern = r"\btropical\b"
text = "A tropical cyclone is a rapidly rotating storm system that forms over warm Tropical or subtropical waters."

# print(re.search(pattern, text))  # Returns only the first occurence of the match from anywhere in the string

# print(re.findall(pattern, text))  # Returns all the matches from anywhere in the string

# print(re.split(pattern, text))  # Returns a list where the string has been split at each match

'''matches = re.finditer(pattern, text)  # Returns an iterator that yields the match objects and gives detailed information of all the matches
for match in matches:
    # print(match)
    # print(match.span())  # Returns a tuple that contains the start and end position of the match
    print(type(match.span()))'''

'''line = "cyclone is a rapidly rotating storm system that forms over warm tropical rapidly"'''
# print(re.sub(r"rap\w+", "fastly", line))  # Replaces one or more matches with a string

'''match = re.match(pattern, line)  # Looks for the pattern only at the beginning of the string. If it doesn't match returns "None"
# print(match.span())  # Returns a tuple containing the start and end position of the match
print(match.group())  # Returns a part of the string where there was match'''

# print(text[99:105])