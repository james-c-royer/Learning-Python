import random, time

options = ("rock", "paper", "scissors")
playerChoice = None
computerChoice = random.choice(options)
continueChoice = ""


while True:
    playerChoice = input(f"Please select an option from {options}: ").lower()

    if playerChoice not in options:
        playerChoice = input(f"Invalid choice! Please select an option from {options}: ").lower()
        continue
    print("Rock...")
    time.sleep(1)
    print("Paper...")
    time.sleep(1)
    print("Scissors...")
    time.sleep(1)
    print("Shoot!")
    time.sleep(1)

    if playerChoice == computerChoice:
        print(f"You played {playerChoice} and the computer played {computerChoice}")
        continueChoice = input("Tie game! Play again? (y/n) ").lower()
        if continueChoice == "n":
            break

    elif playerChoice == "paper" and computerChoice == "scissors":
        print(f"You played {playerChoice} and the computer played {computerChoice}")
        continueChoice = input("You lose! Play again? (y/n) ").lower()
        if continueChoice == "n":
            break

    elif playerChoice == "scissors" and computerChoice == "rock":
        print(f"You played {playerChoice} and the computer played {computerChoice}")
        continueChoice = input("You lose! Play again? (y/n) ").lower()
        if continueChoice == "n":
            break

    elif playerChoice == "rock" and computerChoice == "paper":
        print(f"You played {playerChoice} and the computer played {computerChoice}")
        continueChoice = input("You lose! Play again? (y/n) ").lower()
        if continueChoice == "n":
            break
    
    elif playerChoice == "paper" and computerChoice == "rock":
        print(f"You played {playerChoice} and the computer played {computerChoice}")
        continueChoice = input("You win! Play again? (y/n) ").lower()
        if continueChoice == "n":
            break
    
    elif playerChoice == "rock" and computerChoice == "scissors":
        print(f"You played {playerChoice} and the computer played {computerChoice}")
        continueChoice = input("You win! Play again? (y/n) ").lower()
        if continueChoice == "n":
            break

    elif playerChoice == "scissors" and computerChoice == "paper":
        print(f"You played {playerChoice} and the computer played {computerChoice}")
        continueChoice = input("You win! Play again? (y/n) ").lower()
        if continueChoice == "n":
            break

