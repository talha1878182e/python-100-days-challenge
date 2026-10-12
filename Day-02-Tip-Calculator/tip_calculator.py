print("***Welcome to tip and bill calculator***")
bill = float(input("What was the total bill?"))
tip = float(input("How much tip would you like? 10,12 or 15?"))
people = float(input("How many people to split the bill?"))

total_one_person = (bill + tip) / people

print(f"Each person should pay: ${total_one_person}")
