def display_numbers(numbers):
    for number in numbers:
        if number > 500:
            break  # Stop the loop if the number is greater than 500
        if number > 150:
            continue  # Skip the number if it is greater than 150
        if number % 5 == 0:
            print(number)

# Test the function with the given numbers list
numbers = [12, 75, 150, 180, 145, 525, 50]
display_numbers(numbers)
