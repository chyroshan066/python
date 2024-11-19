numbers = [1, 2, 3, 4, 5]

'''for item in numbers:
    print(item)
    if item == 4:
        break  # When loop breaks then else statement is not executed
else:  # This statement is executed when loop is completed
    print("No more items")'''

i = 0
while i < len(numbers):  # else statement also works with while loop
    print(numbers[i])
    i += 1
    '''if i == 4:
        break'''
else:
    print("No more items")