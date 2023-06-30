def generate_fibonacci(n):
    # Initialize the sequence with the first two numbers
    fibonacci_seq = [0, 1]

    # Generate the Fibonacci sequence
    for i in range(2, n):
        next_number = fibonacci_seq[i-1] + fibonacci_seq[i-2]
        fibonacci_seq.append(next_number)

    return fibonacci_seq[:n]

# Test the function
input_number = 5
fibonacci_sequence = generate_fibonacci(input_number)
print(fibonacci_sequence)
