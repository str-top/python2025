with open('input.txt', 'r') as f:
    f.write('asasasa')
    for line in f:
        print(line.strip())
        with open('numbers.txt', 'r') as f:
            if re.search(r'\d', line):
                f.write(line)
