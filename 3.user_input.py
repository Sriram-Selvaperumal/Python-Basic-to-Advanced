# User Inputs in Python

# 1. Basic User Input:
# The `input()` function is used to take user input as a string.
user_name = input("Enter your name: ")
print("Hello, " + user_name)

# 2. Converting Input to Integer:
# Use `int()` to convert the input to an integer.
user_age = int(input("Enter your age: "))
print("You will be " + str(user_age + 1) + " next year.")

# 3. Converting Input to Float:
# Use `float()` to handle decimal numbers.
user_height = float(input("Enter your height in meters: "))
print("Your height is: " + str(user_height) + " meters.")

# 4. Taking Multiple Inputs:
# Use `split()` to take multiple inputs in one line.
x, y = input("Enter two numbers separated by a space: ").split()
print("First number:", x)
print("Second number:", y)

# 5. Using a List to Store Multiple Inputs:
# The `split()` method can also store inputs in a list.
numbers = input("Enter three numbers separated by spaces: ").split()
print("Numbers entered:", numbers)

# 6. Handling Input Errors:
# Use try-except to handle invalid input errors.
try:
    num = int(input("Enter an integer: "))
    print("You entered:", num)
except ValueError:
    print("That's not an integer!")

# 7. Input with Default Value:
# Use a prompt that explains default behavior.
user_input = input("Press Enter to accept default value (default=10): ") or "10"
print("You entered:", user_input)

# 8. Input with Specific Data Type and Validation:
# Combine data type conversion with validation logic.
while True:
    try:
        marks = float(input("Enter your marks (0-100): "))
        if 0 <= marks <= 100:
            print("Your marks:", marks)
            break
        else:
            print("Please enter a value between 0 and 100.")
    except ValueError:
        print("Invalid input. Please enter a number.")

# Summary:
# - Use `input()` for user input (always returns a string).
# - Convert input to desired type using `int()`, `float()`, etc.
# - Handle errors using `try-except`.
# - Use `split()` to take multiple inputs or store them in a list.
