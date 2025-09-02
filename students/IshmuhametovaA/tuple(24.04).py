with open('file.txt', 'r') as file:
    lines = file.readlines()
for line in reversed(lines):
    print(line, end='')
