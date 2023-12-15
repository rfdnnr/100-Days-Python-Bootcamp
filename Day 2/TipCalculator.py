print("Welcome to my tip calculator, by Rafael Donner!")
TotalBill = float(input("What was the total bill?\n$"))
Tip = int(input("What percentage tip would you like to give? 10, 12 or 15?\n"))
PeopleSplit = int(input("How many people to split the bill?\n"))

FinalValue = (TotalBill*(Tip/100+1))/PeopleSplit



print(f"Each person should pay {round(FinalValue,2)}.")