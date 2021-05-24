"""
Calculator app
"""

#Add function
def add(n1, n2):
    return n1 + n2

#Substract function
def substract(n1, n2):
    return n1 - n2

#Multiply function
def multiply(n1, n2):
    return n1 * n2

#Divide function
def divide(n1, n2):
    return n1 / n2

operations = {
    "+" : add,
    "-" : substract,
    "*" : multiply,
    "/" : divide
}

def calculator():
    num1 = float(input("What's the first number? "))
    for x in operations:
        print(x)
    should_continue = True

    while should_continue:
        symbol = input("Choose your operation: ")

        num2 = float(input("What's the next number? "))
        calculation = operations[symbol]
        answer = calculation(num1, num2)

        print(f"{num1} {symbol} {num2} = {answer}")
        
        if input(f"Type 'y' to contiue calculating with {answer}, or type 'n' to start a new calculation. ") == "y":
            num1 = answer
        else:
            should_continue = False
            calculator()

calculator()


