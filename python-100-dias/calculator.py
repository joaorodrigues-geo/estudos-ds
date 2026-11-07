logo = r"""
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""


def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2
def modulus(n1, n2):
    return n1 % n2

operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide,
    "%" : modulus
}

def calculator():
    print(logo)
    for symbol in operations:
        print(symbol)
    should_continue = True
    n1 = float(input("Enter first number: "))

    while should_continue:
        for symbol in operations:
            print(symbol)
        operation = input("Pick one operation from the above: ")

        if operation not in operations:
            print("Invalid operation. Please try again.")
            continue
        n2 = float(input("Enter second number: "))

        answer = operations[operation](n1, n2)
        print(f"{n1} {operation} {n2} = {answer}")

        choice = input(f"Type 'y' to continue calculating with {answer}, type 'n' to start a new calculation, or type 'e' to exit: ").lower()

        if choice == "y":
            n1 = answer
        elif choice == "n":
            should_continue = False
            calculator()
        else:
            should_continue = False
            print("Goodbye!")

calculator()
