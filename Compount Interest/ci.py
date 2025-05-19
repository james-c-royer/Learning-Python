# calculate compound interest 

principle = 0
rate = 0
time = 0

while principle == 0 or rate == 0 or time == 0:
    if principle <= 0:
        principle = int(input("Enter initial balance: "))
    if rate <= 0:
        rate = float(input("Enter the interest rate as a decimal: ."))
    if time <= 0:
        time = int(input("Enter the number of times the balance is compounded per year: "))

total = principle * pow((1 + rate/100), time)
print(f"${total:,.2f}")