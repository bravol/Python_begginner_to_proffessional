import logo_image

# todo-1 Write out the functions add, subtract, multiply and divide
def add(a,b):
    return a + b
def subtract (a,b):
    return a - b

def multiply(a,b):
    return a * b
def divide(a,b):
    return a / b

# todo-2 Add these 4 functions into a dictionary as values, Keys = "+", "-", "*", "/"
# create a dictionary
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

# todo-3 use the dictionary operations to perform calculations
# print(operations["*"](2,5))
def calculator():
    print(logo_image.calculator_logo)
    should_accumulate = True
    n1 = float(input("What is the first number?: "))
    while should_accumulate:
        # printing all the symbols of operations
        for symbol in operations:
            print(symbol)

        operational_symbol = input("Pick an operation: ")

        n2 = float(input("What is the second number?: "))
        answer = operations[operational_symbol](n1,n2)
        print(f" {n1} {operational_symbol} {n2} = {answer}")

        choice = input(f"Type 'yes' to continue calculating with {answer}, or type 'new' to start new calculation:\n ").lower()

        if choice == 'yes':
            n1 = answer
        else:
            should_accumulate = False
            print("\n" * 20)
            calculator() # calling a function in itself is called recursion. this restarts the calculator function again to do another calculation

calculator()