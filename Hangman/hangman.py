from wordlist import word
import random

# done so the guessing isn't case sensitive. Could also just
# make word lower in the wordlist which would be marginally faster
secretWord = word.lower()

# list used to hold known letters
knownLetters = []

# list to hold guessed letters
guessedLetters = []

# hold value for guessed secretWords
guess = ""

# hold value for incorrect guesses
incorrectGuesses = 0


for char in secretWord:
    knownLetters.append(" _ ")

# dictionary of key:()
hangman_art = {0: ("  ",
                   "  ",
                   "  "),

               1: (" o ",
                   "  ",
                   "  "),

               2: (" o ",
                   " | ",
                   "  "),

               3: (" o ",
                   " |\\ ",
                   "  "),
               4: (" o ",
                   "/|\\ ",
                   "  "),
               5: (" o ",
                   "/|\\ ",
                   "/ "),
               6: (" o ",
                   "/|\\ ",
                   "/ \\ "),}

print(secretWord)
print("Let's play hangman! Your secret secretWord has been generated...")


while True:
    print(knownLetters)
    guess = input("Guess a letter: ")
    
    if len(guess) > 1:
        while len(guess) != 1:
            guess = input("Guess a SINGLE letter: ")
    elif guess in guessedLetters:
        print("You have already guessed that letter! Pick a different one")
        print(f"Currently guessed letters: {guessedLetters}")
        guess = input("Guess a letter: ")
        if len(guess) > 1:
            while len(guess) != 1:
             guess = input("Guess a SINGLE letter: ")
    
    # if the letter guessed is in the secretWord, then find the indices
    # where it is at and changes knownLetters to match
    if guess in secretWord:
        print(f"\"{guess}\" is in the word!")
        for index, char in enumerate(secretWord):
            if guess == secretWord[index]:
                knownLetters[index] = char

    else:
        incorrectGuesses+=1
        print("Incorrect! Printing hangman art:")
        for line in hangman_art[incorrectGuesses]:
            print(line)
    
    if incorrectGuesses > 5:
        print("You lose!")
        break
    elif " _ " not in knownLetters:
        print(f"You win! The word was \"{secretWord}\"")
        break

    guessedLetters.append(guess)
    print(f"You have guessed the following letters: {guessedLetters}")
