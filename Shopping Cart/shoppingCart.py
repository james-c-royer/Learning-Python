continueShopping = True
shoppingDecision = ""
shoppingCart = set()
numItems = 0
itemCost = 0
totalCost = 0

while continueShopping == True:
    shoppingDecision = input("Would you like to add another item to the cart? \"No\" for no, \"Yes\" for yes: ")
    if shoppingDecision == "No":
        continueShopping == False

    elif shoppingDecision == "Yes":
        continueShopping == True

    else:
        print("Invalid option: \"No\" or \"Yes\"")
        continue

    if continueShopping == True:
        shoppingCart.add(input("Enter the item: "))
        numItems += 1
        itemCost = float(input("Enter the item's cost: "))
        totalCost += itemCost
        print("Total number of items in cart is " + str(len(shoppingCart)))
        print(f"Total cost is {totalCost:,.2f}")
        print(f"Current items in cart: {shoppingCart}")
        
    else:
        continueShopping == False 
        break