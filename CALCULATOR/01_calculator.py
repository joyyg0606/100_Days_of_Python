import os

#add
def add(n1, n2):
    return n1 + n2

#subtract
def subtract(n1, n2):
    return n1 - n2

#multiply
def multiply(n1, n2):
    return n1 * n2

#divide 
def divide(n1, n2):
    return n1 / n2

#dict of operations
operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
}

def calculator():
    import calculator_art
    print(calculator_art.logo)

    num1 = float(input("Enter a number: "))

    for sign in operations:
        print(sign)

    should_continue = True
    while should_continue == True:
        operation_sign = input("Enter one of the operations displayed above: ")
        num2 = float(input("Enter the next number: "))
        calculation_function = operations[operation_sign]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_sign} {num2} = {answer}")
        
        continue_calc = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ").lower()

        if continue_calc == 'y':
            num1 = answer
        
        else:
            should_continue = False
            os.system('cls||clear')
            calculator()

calculator()