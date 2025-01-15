# Notes on User Input in Python

Python provides a built-in function `input()` to accept user input from the console. The input entered by the user is always returned as a string, regardless of the type of data entered.

## Syntax
```python
input(prompt)
```
- **prompt** (optional): A string displayed to the user as a message before taking input.

## Example Usage
```python
# Accepting user input
data = input("Enter your name: ")
print("Hello, " + data + "!")
```

### Output Example:
```
Enter your name: Alice
Hello, Alice!
```

---

## Converting User Input
Since `input()` always returns a string, you may need to convert it to the desired type using typecasting functions like `int()`, `float()`, etc.

### Example:
```python
# Accepting an integer input
num = int(input("Enter a number: "))
print("The square of the number is:", num ** 2)
```

### Output Example:
```
Enter a number: 5
The square of the number is: 25
```

---

## Handling Multiple Inputs
You can take multiple inputs in one line by using the `split()` method.

### Example:
```python
# Accepting multiple inputs
x, y = input("Enter two numbers separated by space: ").split()
print("You entered:", x, "and", y)
```

### Output Example:
```
Enter two numbers separated by space: 10 20
You entered: 10 and 20
```

To convert these inputs to integers:
```python
x, y = map(int, input("Enter two numbers separated by space: ").split())
print("Sum:", x + y)
```

---

## Advanced Input Handling

### Using Default Separator
You can specify a custom separator with `split()` by providing it as an argument.

```python
# Accepting inputs separated by commas
x, y, z = input("Enter three values separated by commas: ").split(",")
print("You entered:", x, y, z)
```

---

### Handling Errors
To avoid crashes when invalid input is entered, use exception handling:

```python
try:
    num = int(input("Enter an integer: "))
    print("You entered:", num)
except ValueError:
    print("Invalid input! Please enter an integer.")
```

---

## Key Points
1. **Default Type**: The `input()` function returns data as a string.
2. **Type Conversion**: Use typecasting functions (e.g., `int()`, `float()`, `bool()`) to convert input to the desired type.
3. **Error Handling**: Use `try-except` blocks to handle invalid inputs gracefully.
4. **Multiple Inputs**: Use the `split()` method or `map()` function for cleaner handling of multiple inputs.

---

This covers the essentials of user input in Python. Happy coding!
