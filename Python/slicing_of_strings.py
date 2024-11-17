course = "Python for Beginners"

print(course[7:15])  # Returns the sliced string where first index is starting index, second is stopping index and third index is step. If step is not mentioned then the default step is 1.
print(course[:15])  # If start value is omitted, then it starts with index 0
print(course[5:])  # if end value is omitted, then it goes to the end
print(course[:])
print(course[-12:-4])
print(course[5:20:2])
print(course[::-1])  # Prints in reverse