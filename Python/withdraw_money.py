class InsufficientBalance(Exception):
    def __init__(self):
        print("Insufficient Balance")

class ReachedAttemptLimit(Exception):
    def __init__(self):
        print("Your attempt limit reached. Try in an hour.")

try:
    userBalance = 12000
    userPIN = 1472
    i = 0

    while i < 3:
        enteredPIN = int(input("Enter your PIN: "))
        i += 1

        if userPIN == enteredPIN:
            withdrawAmount = float(input("Enter the amount you want to withdraw: "))

            if withdrawAmount > userBalance-1000:
                    raise InsufficientBalance

            else:
                print(f"Amount successfully withdrawn. \nRemaining Balance: {userBalance - withdrawAmount}")

            break

        else:
            if i == 3:
                print("Wrong PIN.")
                raise ReachedAttemptLimit

            ans = input("Wrong PIN. Do you want to try again: (y/n): ")

            if ans.lower() == 'n':
                break

    else:
        raise ReachedAttemptLimit

except (InsufficientBalance, ReachedAttemptLimit) as var:
    print(var, end="")

