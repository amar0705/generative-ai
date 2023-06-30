def divide_numbers(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Cannot divide by zero."

# Test the function with inputs 5 and 0
result = divide_numbers(5, 0)
print(result)
