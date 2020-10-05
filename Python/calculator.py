def add(x, y):
    # To adds two numbers
    return x + y, '+'


def subtract(x, y):
    # To subtracts two numbers
    return x - y, '-'


def multiply(x, y):
    # To multiplies two numbers
    return x * y, 'x'


def divide(x, y):
    # To divides two numbers
    return x / y, '/'


print("Select your operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Exit")

operation_mapping = {
    '1': add,
    '2': subtract,
    '3': multiply,
    '4': divide,
}

while True:
    # Take input from the user
    choice = input("Enter your choice(1/2/3/4/5): ")

    if choice == '5':
        break

    # Check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        res, sign = operation_mapping[choice](num1, num2)
        print("{} {} {} = {}".format(num1, sign, num2, res))
    else:
        print("Please enter valid choice")
