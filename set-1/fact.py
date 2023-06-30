def factorial(number):
    # Base case: factorial of 0 is 1
    if number == 0:
        return 1

    # Initialize the factorial value
    fact = 1

    # Calculate the factorial using a loop
    for i in range(1, number + 1):
        fact *= i

    return fact

# Test the function
input_number = 5
factorial_result = factorial(input_number)
print("Factorial of", input_number, "is", factorial_result, ".")
