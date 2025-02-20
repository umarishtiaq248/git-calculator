def add(a, b):
    """Add two numbers and return the result."""
    return a + b

def subtract(a, b):
    """Subtract b from a and return the result."""
    return a - b
  
def divide(a, b):
    """Divide a by b and return the result."""
    if b == 0:
        return "Error: Division by zero"
    return a / b

def multiply(a, b):
    """Multiply two numbers and return the result.
    e.g: like in this function a multiply with b and
    result is return
    """
    return a * b

if __name__ == "__main__":
    print("Simple Calculator")
    print("=================")

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    print(f"{num1} + {num2} = {add(num1, num2)}")
    print(f"{num1} - {num2} = {subtract(num1, num2)}")
    print(f"{num1} ÷ {num2} = {divide(num1, num2)}")
    print(f"{num1} × {num2} = {multiply(num1, num2)}")
