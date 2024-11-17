x = "awesome"  # Global Variable
print("Python is " + x)

def myfunc():
    # x = "fantastic"  # Local Variable
    global x  # Using global keyword to change the global variable
    x = "fantastic"
    # print("Python is " + x)

myfunc()
print("Python is " + x)