def showMenu():
    print("********************")
    print("1. Show Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    print("********************")

def showBalance(checkingBalance, savingBalance, decision):
    print("********************")
    print("1. Checking")
    print("2. Savings")
    print("3. Both")
    decision = int(input(("Enter your choice: ")))

    match decision:
        case 1:
            print(f"Checking balance: {checkingBalance:,.2f}")
        case 2:
            print(f"Savings balance: {savingBalance:,.2f}")
        case 3: 
            print(f"Checking balance: {checkingBalance:,.2f}")
            print(f"Savings balance: {savingBalance:,.2f}")
        case _:
            print("Invalid choice")

# silly but just used to practice functions
def deposit(current, change):
    return current + change

def withdraw(current, change):
    return current - change