import datetime

now = datetime.datetime.now()  # Gives current date and time
# print(now.strftime("%Y"))  # Gives full year
# print(now.strftime("%y"))  # Gives year in short form
# print(now.strftime("%b"))  # Gives month in short form
# print(now.strftime("%B"))  # Gives complete month name
# print(now.strftime("%M"))  # Gives minute
# print(now.strftime("%H"))  # Gives hour in 24hr format
print(now.strftime("%I"))  # Gives hour in 12hr format

# print(datetime.datetime(2003, 8, 28))  # Creates date and time object