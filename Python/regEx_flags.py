import re

pattern = r"\btropical\b"
text = "A tropical cyclone is a rapidly rotating storm system that forms over warm Tropical or subtropical waters."

print(re.findall(pattern, text))  # Default is case sensitive matching
# print(re.findall(pattern, text, re.IGNORECASE))  # Does case in-sensitive matching
print(re.findall(pattern, text, re.I))