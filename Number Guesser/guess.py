import random

randomNum = random.randint(0,100)
guessCount = 0

guess = int(input("Guess a number 0 to 100: "))
guessCount+=1

while True:
    if guess > 100 or guess < 0:
        guess = int(input("Your guess is not in range! " \
                          "Guess a number 0 to 100: "))
        guessCount+=1

    elif guess < randomNum:
        guess = int(input("Your guess is too low! " \
                          "Guess a number 0 to 100: "))
        guessCount+=1

    elif guess > randomNum:
        guess = int(input("Your guess is too high! " \
                          "Guess a number 0 to 100: "))
        guessCount+=1
        
    else:
        print(f"Your guess was correct! The number was {randomNum}. You took {guessCount} guesses")
        break