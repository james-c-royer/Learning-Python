menu = {"popcorn":2.50, 
        "soda":1.50, 
        "candy": 1.25,
        "pizza": 1.50,
        "lemonade": 1.50}

ordering = True
progSelection = 0
itemSelection = ""
cart = {}
totalPrice = 0

print("Welcome to the concession stand! " \
    "What can we do for you? \n" \
    "1: Order an item \n2: Remove an item\n" \
    "3: Show cart and item prices\n4: Finalize purchase")
while ordering:
    progSelection = input("\nSelect (1, 2, 3, or 4): ")

    if progSelection == "1":
        print("\nPlease select an item from the menu: ")
        for item, price in menu.items():
            print(f"{item}: ${price:,.2f}")
        itemSelection = input("What item would you like? ")
        if menu.get(itemSelection.lower()) == None:
            print("Not a valid item")
        else:
            cart.update({itemSelection: menu.get(itemSelection.lower())})
    
    elif progSelection == "2":
        print("Here is your current cart: ")

        for item, price in cart.items():
            print(f"Item: {item}, price: ${price:,.2f}")
        
        itemSelection = input("\nWhat item from your cart would you like to remove? ").lower()
        
        if cart.get(itemSelection) == None:
            print("You don't have any of those in the cart!")
        else:
            cart.pop(itemSelection)

    elif progSelection == "3":
        print("Here is your current cart: ")

        for item, price in cart.items():
            print(f"Item: {item}, price: ${price:,.2f}")

    elif progSelection == "4":
        if bool(cart) == False:
            print("You didn't select anything! Goodbye")

        else:
            print("Your final cart is: ")

            for item, price in cart.items():
                print(f"Item: {item}, price: ${price:,.2f}")
            
            for price in cart.values():
                totalPrice += price

            print(f"The total cost of the transaction is ${totalPrice:,.2f}. Have a great day!")

        break

    else:
        print("\nNot a valid selection. Options are as follows:\n" \
        "1: Order an item \n2: Remove an item\n" \
        "3: Show cart and item prices\n4: Finalize purchase")


