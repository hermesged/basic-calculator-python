def calculator():
    
    operations = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y if y != 0 else "Error: Division by zero is not allowed."
    }
    
    print('Welcome to the calculator programme!')
    nombre1 = float(input('Please enter the first number: '))    
    nombre2 = float(input('Please enter the second number: '))
    operation = input('Please enter the operation you want to perform (+, -, *, /): ')
    
    if operation in operations:
        result = operations[operation](nombre1, nombre2)
    else:
        print("Error: Invalid operation.")
        return
    print(f"The result is: {result}")
    
calculator()
