def count_words(input_file, output_file):
    # Read the input file
    with open(input_file, 'r') as file:
        content = file.read()

    # Count the number of words
    word_count = len(content.split())

    # Write the word count to the output file
    with open(output_file, 'w') as file:
        file.write("Number of words: " + str(word_count))

# Specify the input and output file names
input_file = "input.txt"
output_file = "output.txt"

# Call the count_words function
count_words(input_file, output_file)
