import random
import string

# The string module contains punctuation characters, digits,
# and letters as ascii

# this string includes all letters, punctuation, and digits
chars =  string.punctuation + string.ascii_letters + string.digits

#print(chars): !"':/.,`~[]\;1234567890asdfghjklQWERTYUIOP etc etc

# seperates all the characters into individual chars that are
# contained as a list
chars = list(chars)

# copies the list of chars and makes it a key
key = chars.copy()

# shuffles the key
random.shuffle(key)

plainText = input("Please enter a string: ")
encryptedMessage = ""

# iterates through every char in plainText
for letter in plainText:
    # index value = the index of the current letter
    index = chars.index(letter)

    # adds the randomized character to encrypteMessage
    encryptedMessage += key[index]
print(encryptedMessage)

decryptedMessage = ""

for letter in encryptedMessage:
    index = key.index(letter)

    decryptedMessage += chars[index]

print(decryptedMessage)
