course = "          Roshan Is A Good Boy          "

# print(course.upper())  # Converts string to uppercase

# print(course.lower())  # Converts string to lowercase

# print(course.find('for'))  # Finds the index of the character/word in the string

# print(course.replace('for', 'with'))  # Replace the old value in the string with the new value

# print('for' in course)  # Checks whether the character/words exist in the string or not

# print(course[-1])  # Gives the character present in that index of the string

# print(len(course))  # Gives the length of the string

'''splittedText = course.split(",")
print(splittedText)  # Splits the string and returns array if it finds the character specified
for x in splittedText:
    print(x)'''

# print(course.strip())  # Removes whitespaces

# print(course.capitalize())  # Converts the first letter of the string to uppercase and any other letters to lowercase

# print(course.casefold())  # Converts to lowercase

# print(course.center(len(course) + 10, '*'))  # Returns a centered formatted string
# print(course.center(len(course) + 10))

# print(course.zfill(len(course) + 5))  # Fills 0 at the left of the string
'''negNum = "-359"
print(negNum.zfill(len(negNum) + 5))  # If there is any symbol in the prefix then that symbol is printed first and then 0'''

# print(course.count("n"))  # Returns the occurence of substring in a string
# print(course.count("n", 7, len(course)))

# print(list(enumerate(course)))  # Provides the index of characters present in the string

# print(course.encode('utf-8'))  # Returns an encoded version of the string
'''hindi_sentence = "एक बालक खेल रहा था।"
# print(hindi_sentence.encode('ascii', 'ignore'))  # ignores the character that cannot be encoded
print(hindi_sentence.encode('ascii', 'replace'))  # replaces the character with question mark that cannot be encoded'''

# print(course.startswith("for"))  # Returns true if the string starts with the specified value

# print(course.endswith("python"))  # Returns true if the string ends with the specified value

'''tabString = "H\te\tll\to"
print(tabString)
print(tabString.expandtabs())
print(tabString.expandtabs(4))
print(tabString.expandtabs(8))
print(tabString.expandtabs(12))'''

# print(course.isalpha())  # Returns true if all the character in string is alphabet

# print(course.isalnum())  # Returns true if the characters in string is either alphabet or numbers

# print(course.isdigit())  # Returns true if all the character in string is number

# print(course.isascii())  # Returns true if all the character present in the string is ascii character

# print(course.isdecimal())  # Returns true if all the character present in the string is decimal

# print(course.isidentifier())  # Returns true if the string is a valid identifier (i.e it contains only alphanumeric characters or underscores)

# print(course.islower())  # Returns true if all the character present in the string are lowercase letters

# print(course.isnumeric())  # Returns true if all the character in the string is numeric

# print(course.isprintable())  # Returns true if all the character in the string are printable. Carriage return and newline characters are not printable

# print(course.isspace())  # Returns true if all the character present in the string are whitespaces

# print(course.isupper())  # Returns true if all the character in the string are in uppercase letters

# print(course.istitle())  # Returns true if the string follows the rule of the title (i.e first character of the word is in uppercase and other is in lowercase)

'''list = ["Apple", "Ball", "Cat"]
print("; ".join(list))  # Joins the element of the iterable at the end of the string separated by the string specified'''
'''dict = {"Australia": 5, "West Indies": 2, "India": 2}
print(", ".join(dict))'''

# print(course.ljust(len(course) + 10, "I"))  # Returns a left justified version of the string

# print(course.rjust(len(course) + 10))  # Returns a right justified version of the string

# print(course.lstrip())  # Returns a left trim version of the string

print(course.rstrip())  # Returns a right trim version of the string

print(course)