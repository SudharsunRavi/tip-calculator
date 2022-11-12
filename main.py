print("Welcome to tip calculator")
bill = int(input("What is the total bill value? $"))
tip = int(input("What percentage would you like to tip? "))
ppl = int(input("How many members? "))
tper = (tip) / 100
billamt = (tper) * (bill)
billamt2 = (billamt) + (bill)
billamt3 = (billamt2) / (ppl)
print("Each has to pay $", billamt3)
