# Variables in Python

# 1. Variable Declaration:
# Variables are created when you assign a value to them.
name = "Alice"   # String
age = 25         # Integer
height = 5.5     # Float
is_student = True  # Boolean

# 2. Dynamic Typing:
# Python is dynamically typed, so variables can hold values of any type.
x = 10           # Integer
x = "Hello"      # Now x is a string
x = 3.14         # Now x is a float

# 3. Naming Rules:
# Variable names must start with a letter or underscore (_) and can contain letters, digits, and underscores.
_valid_name = "Valid"
name2 = "Also valid"

# Invalid names:
# 2name = "Invalid"    # Cannot start with a digit
# name! = "Invalid"    # Special characters are not allowed

# 4. Case Sensitivity:
# Variable names are case-sensitive.
Var = 10
var = 20
print(Var)  # Output: 10
print(var)  # Output: 20

# 5. Multiple Assignment:
# Assign values to multiple variables in one line.
a, b, c = 1, 2, 3
print(a, b, c)  # Output: 1 2 3

# Assign the same value to multiple variables.
x = y = z = 100
print(x, y, z)  # Output: 100 100 100

# 6. Constants:
# By convention, constants are written in uppercase (not enforced by Python).
PI = 3.14159
GRAVITY = 9.8

# 7. Type Checking:
# Use `type()` to check the type of a variable.
my_var = 42
print(type(my_var))  # Output: <class 'int'>

# 8. Mutable and Immutable Variables:
# Mutable (e.g., list) - Can be modified after assignment.
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)  # Output: [1, 2, 3, 4]

# Immutable (e.g., string) - Cannot be modified after assignment.
my_str = "Hello"
# my_str[0] = 'h'  # This will raise an error.

# 9. Variable Scope:
# Variables defined inside a function are local to that function.
def my_function():
    local_var = 10
    print(local_var)

my_function()
# print(local_var)  # Error: local_var is not defined outside the function.

# Global variable (defined outside any function).
global_var = "I am global"

def access_global():
    print(global_var)  # Can be accessed inside a function.

access_global()

# 10. Best Practices:
# - Use meaningful variable names (e.g., "age" instead of "a").
# - Use lowercase with underscores for variable names (e.g., "user_name").
# - Follow Python's naming conventions (PEP 8).

# Summary:
# - Variables are used to store data.
# - Python allows dynamic typing.
# - Use meaningful names and follow naming conventions.
