secret_number = 12
guess_count= 0
guess_limit = 3

while guess_count< guess_limit:
    entered_number = int(input("Guess: "))
    guess_count += 1
    if entered_number == secret_number:
        print("You win!")
        break
else:
    print("Sorry you failed!")