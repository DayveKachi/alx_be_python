num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /): ")
zerodivflag = False

match operation:
    case "+":
        result = num1 + num2
    case "-":
        result = num1 - num2
    case "*":
        result = num1 * num2
    case "/":
        if num2 == 0:
            zerodivflag = True
            print("Cannot divide by zero.")
        else:
            result = num1 / num2

if not zerodivflag:
    print(f"The result is {result}.")
