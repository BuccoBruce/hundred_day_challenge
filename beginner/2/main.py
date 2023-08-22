print("Welcome to the tip calculator.")

totalBill = float(input("What was the total bill? $"))
peopleSplit = int(input("How many people to split the bill? "))
# Add one to percent to get correct multiplier
percentTip = 1 + float(input("What percentage tip would you like to give? 10, 12, or 15? ")) / 100

# Round total each person must pay to 1 significant digit
totalToPay = round((totalBill * percentTip) / peopleSplit, 2)

# Reduce significant digits of totalToPay to 1 in output
print(f"Each person should pay: ${totalToPay}")