print("Welcome to the Ultra Fast Rollercoaster")
height = int(input("What is your height in cm?"))

bill = 0

if height > 120:
    age = int(input("What is your age?"))
    if age >=18:
        weight = int(input("What is your weight?"))
        if weight <= 50:
            print("You can ride the Ultra Fast Rollercoaster")
            print("And you pay 10$")
            bill += 10
        elif weight <= 90:
            print("You can ride the Ultra Fast Rollercoaster")
            print("And you pay 15$")
            bill += 15
        want_foto = input("Do you want to have a photo take? Type y for Yes or n for No")
        if want_foto == "y":
            bill += 5
            print(f"You final bill is {bill}")

        else :
            print("Sorry you can't ride the Ultra Fast Rollercoaster")
    else:
        print("Sorry you can't ride the Ultra Fast Rollercoaster")
else:
    print("Sorry you can't ride the Ultra Fast Rollercoaster")
