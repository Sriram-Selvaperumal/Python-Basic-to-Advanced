# Type Casting in Python

# 1. Introduction:
# Type casting is the process of converting one data type to another.

# 2. Implicit Type Casting:
# Python automatically converts one data type to another when no data is lost.
num_int = 10       # Integer
num_float = 3.5    # Float
result = num_int + num_float  # Python implicitly converts `num_int` to a float
print(result)      # Output: 13.5
print(type(result))  # Output: <class 'float'>

# 3. Explicit Type Casting:
# Use built-in functions to manually convert between types.

# a. Convert to Integer:
float_num = 7.8
int_num = int(float_num)  # Truncates the decimal part
print(int_num)            # Output: 7

str_num = "100"
int_from_str = int(str_num)
print(int_from_str)       # Output: 100

# Note: Invalid conversions will raise an error.
# invalid_int = int("abc")  # ValueError

# b. Convert to Float:
int_num = 42
float_num = float(int_num)  # Adds a decimal point
print(float_num)            # Output: 42.0

str_float = "3.14"
float_from_str = float(str_float)
print(float_from_str)       # Output: 3.14

# c. Convert to String:
num = 25
str_num = str(num)
print(str_num)              # Output: "25"
print(type(str_num))        # Output: <class 'str'>

# d. Convert to List:
str_val = "Hello"
list_val = list(str_val)  # Converts a string to a list of characters
print(list_val)           # Output: ['H', 'e', 'l', 'l', 'o']

# e. Convert to Tuple:
list_val = [1, 2, 3]
tuple_val = tuple(list_val)
print(tuple_val)          # Output: (1, 2, 3)

# f. Convert to Set:
list_val = [1, 2, 2, 3]
set_val = set(list_val)   # Removes duplicates
print(set_val)            # Output: {1, 2, 3}

# g. Convert to Boolean:
# Non-zero numbers, non-empty collections, and `True` evaluate to `True`.
bool_val = bool(10)       # True
bool_val2 = bool(0)       # False
bool_val3 = bool("")      # False
bool_val4 = bool("Python")  # True
print(bool_val, bool_val2, bool_val3, bool_val4)

# 4. Type Checking:
# Use the `type()` function to check a variable's data type.
value = 3.14
print(type(value))  # Output: <class 'float'>

# 5. Example Use Case:
# Get user input, convert to integer, and perform a calculation.
user_input = input("Enter a number: ")  # Always returns a string
user_num = int(user_input)             # Explicitly convert to integer
print("Double the number:", user_num * 2)

# Summary:
# - Implicit casting happens automatically.
# - Explicit casting requires built-in functions like `int()`, `float()`, `str()`, etc.
# - Use `type()` to verify the data type of a variable.
# - Handle potential errors during casting (e.g., converting "abc" to an integer).
