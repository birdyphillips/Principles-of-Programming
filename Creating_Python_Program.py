# Part 1: Addition and Subtraction
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

addition = num1 + num2
subtraction = num1 - num2

print("Addition:", addition)
print("Subtraction:", subtraction)

# Part 2: Multiplication and Division
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

multiplication = num1 * num2
if num2 != 0:
    division = num1 / num2
    print("Multiplication:", multiplication)
    print("Division:", division)
else:
    print("Multiplication:", multiplication)
    print("Division: Cannot divide by zero.")

