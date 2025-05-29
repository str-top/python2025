with open('input.txt', 'r') as input_file, open('numbers.txt', 'w') as numbers_file:
    for line in input_file:
        if any(char.isdigit() for char in line):
            numbers_file.write(line)
