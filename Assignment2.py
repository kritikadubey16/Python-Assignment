# Read the content of file1.txt
file_path = 'file1.txt'

with open(file_path, 'r') as file:
    content = file.read()

# Reverse the content
reversed_content = content[::-1]

# Write the reversed content back to file1.txt
with open(file_path, 'w') as file:
    file.write(reversed_content)

print(f"The contents of {file_path} have been reversed and updated in the file.")

#Problem 3
# Define the file path
file_path = 'file3.txt'

# Initialize an empty dictionary to store key-value pairs
data_dict = {}

# Read the contents of the file and create a dictionary
with open(file_path, 'r') as file:
    for line in file:
        # Split each line by ':' assuming key-value pairs separated by ':'

#Problem 2

# Define a function to convert numbers to words
def number_to_words(num):
    # Dictionary mapping numbers to their textual representation
    number_words = {
        '0': 'zero', '1': 'one', '2': 'two', '3': 'three', '4': 'four',
        '5': 'five', '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine'
    }

    # Check if the input num is a digit
    if num.isdigit():
        return number_words[num]
    else:
        return num  # If not a digit, return the original value

# Define the file path
file_path = 'file2.txt'

# Read the contents of the file and convert numbers to words
with open(file_path, 'r') as file:
    content = file.read()
    words_content = ' '.join(number_to_words(char) for char in content.split())

# Write the converted content back to file2.txt
with open(file_path, 'w') as file:
    file.write(words_content)

print(f"Numbers in {file_path} have been converted to text.")