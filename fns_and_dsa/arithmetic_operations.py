# This module performs basic arithmetic operations


def perform_operation(num1, num2, operation):
    """This function takes 2 numbers(num1 and num2 respectively)
    and one operation('add', 'subtract', 'divide', 'multiply')
    and returns the result of the operation on the 2 numbers."""

    match operation:
        case "add":
            result = num1 + num2
        case "subtract":
            result = num1 - num2
        case "multiply":
            result = num1 * num2
        case "divide":
            if num2 == 0:
                result = "please, you cannot divide by zero!"
            else:
                result = num1 / num2
    return result
