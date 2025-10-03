user_input = input("Enter command: ")  
tokens = user_input.split()

if len(tokens) != 3:
    print("Usage: <operation> <num1> <num2>")
else:
    command, a, b = tokens
    a, b = float(a), float(b)

    if command == "add":
        print(a + b)
    elif command == "sub":
        print(a - b)
    elif command == "mul":
        print(a * b)
    elif command == "div":
        if b != 0:
            print(a / b)
        else:
            print("Error: Division by zero")
    else:
        print(f"Unknown command: {command}")
