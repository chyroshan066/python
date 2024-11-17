# print("Hello World")

# STRING METHODS
course = "python for Beginners"
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
    print(x)
# print(course.strip())  # Removes whitespaces'''
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
# print(course)
# print(course.startswith("for"))  # Returns true if the string starts with the specified value
# print(course.endswith("python"))  # Returns true if the string ends with the specified value
tabString = "H\te\tll\to"
print(tabString)
print(tabString.expandtabs())
print(tabString.expandtabs(4))
print(tabString.expandtabs(8))
print(tabString.expandtabs(12))