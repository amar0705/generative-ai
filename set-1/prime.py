def is_prime_number(number):
    # Check if the number is less than 2
    if number < 2:
        return False

    # Check for factors from 2 to the square root of the number
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False

    return True

# Test the function
input_number = 13
if is_prime_number(input_number):
    print(input_number, "is a prime number.")
else:
    print(input_number, "is not a prime number.")
