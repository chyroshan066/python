# print("Hello World")


# **************Assigning multiple values to variables*************************
# Assigning multiple values to multiple variables at a time
'''x, y, z = "Apple", "Banana", "Orange"
print(x)
print(y)
print(z)'''

# Assigning same values to multiple variables at a time
'''x = y = z = "Apple"
print(x)
print(y)
print(z)'''

# Unpacking a collection
'''fruits = ["Apple", "Banana", "Orange"]
x, y, z = fruits
print(x)
print(y)
print(z)'''
# print(x, z)
'''a = 10
print(x + a)  # Throws an error'''

# *************************************Global Variable***********************************************
'''x = "awesome"  # Global Variable
print("Python is " + x)

def myfunc():
    # x = "fantastic"  # Local Variable
    global x  # Using global keyword to change the global variable
    x = "fantastic"
    # print("Python is " + x)

myfunc()
print("Python is " + x)'''

# ***************************************Program to add two input numbers******************************************
'''num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")
print("Sum = ", float(num1) + float(num2))'''

# **************************************************Strings*******************************************************
# MULTILINE STRINGS
'''multilineString = ("Learning the ins and outs of advanced Jira functionalities, from detailed project tracking to customized workflows, "
                   "has given me a powerful toolkit for effective project management and collaboration. I’m thrilled to bring these skills"
                   " into my future work, ensuring projects run smoothly and teams stay aligned.")'''
# multilineString = '''Learning the ins and outs of advanced Jira functionalities, from detailed project tracking to customized workflows,
# has given me a powerful toolkit for effective project management and collaboration. I’m thrilled to bring these skills into my future work,
# ensuring projects run smoothly and teams stay aligned.'''
'''multilineString = """Learning the ins and outs of advanced Jira functionalities, from detailed project tracking to customized workflows, 
has given me a powerful toolkit for effective project management and collaboration. I’m thrilled to bring these skills into my future work, 
ensuring projects run smoothly and teams stay aligned."""'''
# print(multilineString)

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

#SLICING OF STRINGS
# print(course[7:15])  # Returns the sliced string where first index is starting index, second is stopping index and third index is step. If step is not mentioned then the default step is 1.
# print(course[:15])  # If start value is omitted, then it starts with index 0
# print(course[5:])  # if end value is omitted, then it goes to the end
# print(course[:])
# print(course[-12:-4])
# print(course[5:20:2])
# print(course[::-1])  # Prints in reverse

#FORMAT STRINGS
'''letter = "Hello, my name is {1} and I am from {0}"
name = "Roshan"
country = "Nepal"
cash = 4000.00987
# print(f"Hello, my name is {name} and I am from {country} and I have Rs{cash:.3f}")
print(f"Hello, my name is {{name}} and I am from {{country}} and I have Rs{cash:.3f}")'''
# print(letter.format(country, name))

#ESCAPE CHARACTER
# print('I\'ll call you later')
# print('I\'ll call you \nlater')  # \n is used for new line
# print('I\'ll call you \tlater')  # \t is used for tab
'''x = "no___benefit of study\rHuge_benefit"
print(x)'''