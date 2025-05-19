import math

result = 0
num1 = float(input("What is the first number you would like to use? "))
num2 = float(input("What is the second number you would like to use? "))
operation = input("What operation would you like to do? sqrt, power, add, subtract, multiply, or divide: ")

if operation == "add":
    result = num1 + num2
elif operation == "subtract":
    result = num1 - num2
elif operation == "multiply":
    result = num1 * num2
elif operation == "divide":
    result = num1 / num2
elif operation == "sqrt":
    whichNum = input("Which number would you like the sqrt of? num1 or num2: ")
    if whichNum == "num1":
        result = round(math.sqrt(num1), 3)
    elif whichNum == "num2":
        result = round(math.sqrt(num2), 3)
    else:
        print("Input error: should be num1 or num2")
        exit()
elif operation == "power":
    result = num1 ** num2
else:
    print(f"\"{operation}\" is not a valid choice. Exiting program")
    exit()

print(f"The result is: {result}")

    
