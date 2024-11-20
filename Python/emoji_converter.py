message = input("> ")
message_array = message.split(" ")

emojis = {
    ":)": "😊",
    ":(": "😔"
}

# My approach
'''i = 0
initial_string = ""
while i < len(message_array) - 1:
    initial_string += message_array[i] + " "
    i += 1
else:
    initial_string += emojis[message_array[len(message_array) - 1]]

print(initial_string)'''

# Mosh approach
output = ""
for word in message_array:
    output += emojis.get(word, word) + " "
print(output)