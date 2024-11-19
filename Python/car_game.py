operation = ''
while True:
    present_state = operation
    operation = input('> ').lower()
    if operation == present_state:
        print(f'Hey, car is already {present_state}ed. What are you doing?') if present_state == 'start' else print(f'Hey, car is already {present_state}ped. What are you doing?')
    elif operation == 'start' and operation != present_state:
        print('Car started...Ready to go!')
    elif operation == 'stop' and operation != present_state:
        print('Car stopped')
    elif operation == 'help':
        print("""start - to start the car
stop - to stop the car
quit - to exit
        """)
    elif operation == 'quit':
        break
    else:
        print('I don\'t understand that...')


