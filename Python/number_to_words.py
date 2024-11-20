num_to_word = {
    "0": "Zero",
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine",
}

def digits_to_words(numbers):
    return " ".join(num_to_word[digit] for digit in numbers)

phoneNo = input("Phone: ")
print(digits_to_words(phoneNo))

