import options
import random
from time import sleep

def main():
    choice = 0 # int used by the program to make menu decisions
    amount = float(0) # float used by the program for money changing

    savings = float(random.randint(0,1000000))
    checking = float(random.randint(0, 100000))

    while True:
        options.showMenu()
        choice = int(input("Enter your choice: "))

        match choice:
            case 1:
                options.showBalance(checking, savings, choice)
                
            case 2:
                print("********************")
                amount = round(float(input("Enter deposit amount: ")), 2)
                print("Which account would you like to deposit into?")
                print("1. Checking")
                print("2. Savings")
                choice = int(input("Enter your choice: "))
                
                if choice == 1:
                    checking = options.deposit(current = checking, change = amount)
                elif choice == 2:
                    savings = options.deposit(current = savings, change = amount)                
                else:
                    print("Invalid choice")

            case 3:
                print("********************")
                amount = round(float(input("Enter withdrawal amount: ")),2)
                print("Which account would you like to withdraw from?")
                print("1. Checking")
                print("2. Savings")
                choice = int(input("Enter your choice: "))
                
                if choice == 1 and amount <= checking:
                    checking = options.withdraw(current = checking, change = amount)
                elif choice == 1 and amount > checking:
                    print(f"Attempting to withdraw ${amount} when only ${checking} is in the account.")
                    print("Transaction failed")       
                elif choice == 2 and amount <= savings:
                    savings = options.withdraw(current = savings, change = amount)
                elif choice == 2 and amount > savings:
                    print(f"Attempting to withdraw ${amount} when only ${checking} is in the account.")
                    print("Transaction failed")       
                else:
                    print("Invalid choice")
            case 4:
                break
            case _:
                print("Invalid choice")
        sleep(2)
        


if __name__ == '__main__':
    main()