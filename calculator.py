def calculator():
    print('Welcome to the calclator programme!')
    print('Please enter the first number:')
    nombre1 = float(input())    
    print('Please enter the second number:')
    nombre2 = float(input())
    print('Please enter the operation you want to perform (+, -, *, /):')
    operation = input()
    
    if operation == '+':
        result = nombre1 + nombre2
    elif operation == '-':
        result = nombre1 - nombre2
    elif operation == "*":
        result = nombre1 * nombre2
    elif operation == "/":
        if nombre2 != 0:
            result = nombre1 / nombre2
        else:
            print("Error: Division by zero is not allowed.")
            return
    else:
        print("Error: Invalid operation.")
        return
    print(f"The result is: {result}")
    

