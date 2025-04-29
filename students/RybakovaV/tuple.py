with open('input.txt', 'r') as a:
    with open('numbers.txt', 'w+') as f:
        for line in a:
            if any(char.isdigit() for char in line):
                f.write(line)
        print(f.read())
