def calculator():
    print('Welcome to the calculator programme!')
    nombre1 = float(input('Please enter the first number: '))    
    nombre2 = float(input('Please enter the second number: '))
    operation = input('Please enter the operation you want to perform (+, -, *, /): ')
    
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
    
calculator()
