from art import logo


def add(number1, number2):
    return number1 + number2


def sub(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    return num1/num2


print(logo)
operations = {"+": add,
              "-":sub,
              "*":multiply,
              "/": divide}


def calculator():
    should_continue = "y"
    num1 = float(input("What is your first Number? : "))
    while should_continue == 'y':
        for symbol in operations:
            print(symbol)
        operation = input("Pick and operation : ")
        num2 = float(input("What is the next number? :"))
        get_operation = operations[operation]
        num1 = get_operation(num1, num2)

        should_continue = input(f"Type 'y' is you want to continue with {num1}, or type 'n' to start calculating again: ")

    calculator()

calculator()
