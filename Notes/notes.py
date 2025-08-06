try:    # always executes
    number = int(input("Enter a number to divide 1 by: "))
    print(1 / number)
except TypeError:
    print("That is not a number")
except ZeroDivisionError:
    print("Cannot divide by 0")
except Exception: # catch all that detects ANY exception
    print("Complete")