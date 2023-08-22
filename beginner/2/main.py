print("Welcome to the tip calculator.")
totalBill = float(input("What was the total bill? $"))
peopleSplit = int(input("How many people to split the bill? "))
percentTip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
totalToPay = 0.0

totalToPay = float((totalBill * (1 + (percentTip / 100))) / peopleSplit)

print("Each person should pay: ${:.1f}".format(totalToPay))