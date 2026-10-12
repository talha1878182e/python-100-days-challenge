
def add(n1,n2):
    return n1 + n2
def subtract(n1,n2):
    return n1 - n2
def multiply(n1,n2):
    return n1 * n2
def divide(n1,n2):
    return n1 / n2
def square(n1,n2):
    return n1 ** 2
def square_root(n1,n2):
    return n1 ** (1/2)
operarions = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    "^": square,
    "**": square_root
}
print("""
 _____________________
|  _________________  |
| | JO           0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|
"""
      )

def calculator():
    should_accumulate = True
    num1 = float(input(" What is first number? "))

    while should_accumulate:
        for symbol in operarions:
            print(symbol)
        choose_symbol = input("Pick an operarion: ")
        num2 = float(input(" What is second number? "))
        answer = operarions[choose_symbol](num1, num2)
        print(f"{num1} {choose_symbol} {num2} = {answer}")

        choice = input(f"Type'y' to continue with {answer}, or type 'n' to start a new calculation: ")
        if choice == "n":
            num1= answer
        else:
            should_accumulate = False
            print("\n"*20)
            calculator()
calculator()

