from pathlib import Path

path = Path()  # Creates path object

# print(path.exists())  # Checks whether the path exists or not. Returns boolean value

# print(path.mkdir())  # Creates a new directory. Returns "None"

# print(path.rmdir())  # Removes a directory. Returns "None"

# directory = path.glob('*.py')  # Returns all the python files in the directory
directory = path.glob('*')  # Returns all the files in the directory
for files in directory:
    print(files)